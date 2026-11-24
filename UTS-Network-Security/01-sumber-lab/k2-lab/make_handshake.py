#!/usr/bin/env python3
"""
Membuat capture WPA2 4-way handshake (message 1 & 2) yang SAH secara kriptografi,
untuk keperluan latihan analisis aircrack-ng ketika file resmi dari penguji
tidak tersedia/corrupt. PMK/PTK/MIC dihitung sesuai standar IEEE 802.11i
(PBKDF2-HMAC-SHA1 lalu PRF-384 berbasis HMAC-SHA1), bukan nilai dummy.
"""
import hmac, hashlib, struct, random
from scapy.all import Dot11, Dot11Beacon, Dot11Elt, LLC, SNAP, EAPOL, RadioTap, Raw, wrpcap

SSID = "Lab-K2-WiFi"
PASSWORD = "k2network"          # password asli yang akan "ditemukan" aircrack-ng
AP_MAC = "00:11:22:33:44:55"
STA_MAC = "66:77:88:99:aa:bb"

def mac_to_bytes(mac):
    return bytes.fromhex(mac.replace(":", ""))

def prf_384(pmk, a, b):
    r = b""
    i = 0
    while len(r) < 48:
        r += hmac.new(pmk, a + b"\x00" + b + bytes([i]), hashlib.sha1).digest()
        i += 1
    return r[:48]

# 1. PMK dari passphrase (standar WPA2-PSK)
pmk = hashlib.pbkdf2_hmac("sha1", PASSWORD.encode(), SSID.encode(), 4096, 32)

# 2. Nonce acak (seperti kondisi nyata)
anonce = bytes([random.randint(0,255) for _ in range(32)])
snonce = bytes([random.randint(0,255) for _ in range(32)])

aa, sa = mac_to_bytes(AP_MAC), mac_to_bytes(STA_MAC)
amac_min, amac_max = (aa, sa) if aa < sa else (sa, aa)
anonce_min, anonce_max = (anonce, snonce) if anonce < snonce else (snonce, anonce)

# 3. PTK -> ambil KCK (16 byte pertama) untuk hitung MIC
ptk = prf_384(pmk, b"Pairwise key expansion", amac_min + amac_max + anonce_min + anonce_max)
kck = ptk[:16]

rsn = bytes.fromhex("0100000fac040100000fac040100000fac020000")

# Urutan field EAPOL-Key (IEEE 802.1X): desc(1) + key_info(2) + key_length(2) +
# replay_counter(8) + key_nonce(32) + key_iv(16) + key_rsc(8) + key_id/reserved(8) +
# key_mic(16) + key_data_length(2) + key_data(var)

# --- Message 1 (AP -> STA): bawa ANonce, MIC=0, Ack=1 ---
key_info_m1 = 0x008a
body1 = (struct.pack(">BHH", 2, key_info_m1, 16) + struct.pack(">Q", 1) +
         anonce + b"\x00"*16 + b"\x00"*8 + b"\x00"*8 + b"\x00"*16 + struct.pack(">H", 0))
eapol1 = struct.pack(">BBH", 2, 3, len(body1)) + body1

# --- Message 2 (STA -> AP): bawa SNonce, MIC asli (dihitung dari KCK) ---
key_info_m2 = 0x010a
key_data = struct.pack(">BB", 0x30, len(rsn)) + rsn
body2_for_mic = (struct.pack(">BHH", 2, key_info_m2, 16) + struct.pack(">Q", 1) +
                 snonce + b"\x00"*16 + b"\x00"*8 + b"\x00"*8 + b"\x00"*16 +
                 struct.pack(">H", len(key_data)) + key_data)
eapol2_for_mic = struct.pack(">BBH", 2, 3, len(body2_for_mic)) + body2_for_mic
mic = hmac.new(kck, eapol2_for_mic, hashlib.sha1).digest()[:16]

body2 = (struct.pack(">BHH", 2, key_info_m2, 16) + struct.pack(">Q", 1) +
         snonce + b"\x00"*16 + b"\x00"*8 + b"\x00"*8 + mic +
         struct.pack(">H", len(key_data)) + key_data)
eapol2 = struct.pack(">BBH", 2, 3, len(body2)) + body2

p_beacon = RadioTap()/Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=AP_MAC, addr3=AP_MAC)/Dot11Beacon(cap=0x11)/Dot11Elt(ID="SSID", info=SSID.encode())/Dot11Elt(ID=48, info=rsn)
p_msg1 = RadioTap()/Dot11(type=2, subtype=0, FCfield=2, addr1=STA_MAC, addr2=AP_MAC, addr3=AP_MAC)/LLC(dsap=0xaa, ssap=0xaa, ctrl=3)/SNAP(OUI=0, code=0x888e)/Raw(load=eapol1)
p_msg2 = RadioTap()/Dot11(type=2, subtype=0, FCfield=1, addr1=AP_MAC, addr2=STA_MAC, addr3=AP_MAC)/LLC(dsap=0xaa, ssap=0xaa, ctrl=3)/SNAP(OUI=0, code=0x888e)/Raw(load=eapol2)

wrpcap("handshake-k2-demo.cap", [p_beacon, p_msg1, p_msg2])
print(f"Dibuat: handshake-k2-demo.cap | SSID={SSID} | password asli={PASSWORD}")
