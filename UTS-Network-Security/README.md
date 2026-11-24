# UTS Praktik Infrastruktur & Network Attacks — Kasus 2

Repository ini berisi dokumentasi pengerjaan Ujian Tengah Semester (UTS) Praktik Infrastruktur & Network Attacks / Keamanan Jaringan untuk **Kasus 2**, dengan cakupan praktikum Pertemuan 1 sampai 7.

Repository mencakup source code laboratorium, Dockerfile, konfigurasi Docker Compose, dokumen panduan, hasil pengujian, analisis, dan screenshot sebagai bukti pengerjaan.

> **Peringatan penggunaan:** Seluruh simulasi keamanan jaringan di repository ini ditujukan hanya untuk lingkungan laboratorium lokal yang dibuat sendiri dan diizinkan. Jangan menjalankan pengujian terhadap perangkat, jaringan, atau layanan milik pihak lain tanpa izin.

## Identitas Praktikum

| Informasi | Keterangan |
|---|---|
| Nama | Insanul Firas |
| NIM | 24552011147 |
| Mata Kuliah | Keamanan Jaringan (Security Network) |
| Jenis Ujian | Ujian Tengah Semester (UTS) Praktik |
| Nomor Kasus | Kasus 2 (`k2`) |
| Cakupan Praktikum | Pertemuan 1–7 |
| Sistem Operasi Host | Windows |
| Terminal | Windows PowerShell |
| Lingkungan Container | Docker Desktop |

**Perhitungan nomor kasus berdasarkan NIM:**

- NIM: `24552011147`
- Jumlah digit: `2 + 4 + 5 + 5 + 2 + 0 + 1 + 1 + 1 + 4 + 7 = 32`
- Sisa bagi: `32 mod 10 = 2`
- **Nomor kasus: Kasus 2 (`k2`)**

## Dokumentasi Utama

Dokumentasi utama pengerjaan tersedia pada:

**[`03-hasil kasus-2/jawaban.md`](<03-hasil kasus-2/jawaban.md>)**

File `jawaban.md` menggabungkan dokumentasi Tugas 1 sampai Tugas 7, termasuk identitas, tujuan, dasar teori, perintah yang dijalankan, hasil terminal, analisis, kesimpulan, dan screenshot.

Dokumentasi per tugas juga disimpan secara terpisah pada folder `tugas1/` sampai `tugas7/` agar hasil setiap pertemuan lebih mudah ditinjau.

## Daftar Isi

1. [Identitas Praktikum](#identitas-praktikum)
2. [Dokumentasi Utama](#dokumentasi-utama)
3. [Struktur Repository](#struktur-repository)
4. [Penjelasan Folder](#penjelasan-folder)
5. [Ringkasan Praktikum Pertemuan 1–7](#ringkasan-praktikum-pertemuan-17)
6. [Teknologi dan Tools](#teknologi-dan-tools)
7. [Persiapan Lingkungan Praktikum](#persiapan-lingkungan-praktikum)
8. [Cara Menjalankan Praktikum](#cara-menjalankan-praktikum)
9. [Dokumentasi Hasil Pengerjaan](#dokumentasi-hasil-pengerjaan)
10. [Catatan Praktikum](#catatan-praktikum)
11. [Tujuan Repository](#tujuan-repository)

## Struktur Repository

```text
UTS-Network-Security/
│
├── README.md
│
├── 01-source-lab/
│   └── samples/
│       └── wordlist-k2.txt
│
├── 01-sumber-lab/
│   ├── README.md
│   ├── setup.sh
│   ├── cleanup.sh
│   ├── images/
│   │   ├── uts-openssl/
│   │   │   └── Dockerfile
│   │   ├── uts-kali-tools/
│   │   │   └── Dockerfile
│   │   └── uts-dnsmasq/
│   │       └── Dockerfile
│   ├── b/
│   │   ├── b1-compose/
│   │   │   └── docker-compose.yml
│   │   ├── b3-syn-flood/
│   │   │   └── docker-compose.yml
│   │   └── b4-dns-exfil/
│   │       └── docker-compose.yml
│   ├── kasus/
│   │   ├── k5-scapy/
│   │   │   └── kirim_icmp.py
│   │   └── k9-dns-detect/
│   │       └── analisis_dns.py
│   ├── k2-lab/
│   │   ├── handshake-k2.cap
│   │   ├── make_handshake.py
│   │   └── wordlist-k2.txt
│   └── samples/
│       ├── CAPTURE-FILES-GUIDE.md
│       ├── CASES-CHECKLIST.md
│       ├── handshake-k1.cap ... handshake-k10.cap
│       └── wordlist-k1.txt ... wordlist-k10.txt
│
├── 02-dokumen/
│   ├── DOKUMEN-UTS-LENGKAP.md
│   ├── LEMBAR-PERINTAH-PER-KASUS.md
│   └── PENGUJI-CHECKLIST.md
│
├── 03-hasil kasus-2/
│   ├── jawaban.md
│   ├── tugas1/
│   │   ├── hasil.md
│   │   └── screenshot/
│   ├── tugas2/
│   │   ├── hasil.md
│   │   └── screenshot/
│   ├── tugas3/
│   │   ├── hasil.md
│   │   └── screenshot/
│   ├── tugas4/
│   │   ├── hasil.md
│   │   └── screenshot/
│   ├── tugas5/
│   │   ├── hasil.md
│   │   └── screenshot/
│   ├── tugas6/
│   │   ├── hasil.md
│   │   └── screenshot/
│   └── tugas7/
│       ├── hasil.md
│       └── screenshot/
│
└── cleanup.sh
```

*Catatan: daftar di atas menampilkan struktur utama dan beberapa file penting. Folder `samples/` berisi file capture dan wordlist untuk beberapa kasus; tidak seluruh nama file ditampilkan satu per satu.*

## Penjelasan Folder

| Folder / File | Keterangan |
|---|---|
| `01-source-lab/` | Folder tambahan yang berisi sample wordlist. |
| `01-sumber-lab/` | Direktori utama source laboratorium yang digunakan untuk build image dan menjalankan konfigurasi Docker. |
| `01-sumber-lab/images/` | Berisi Dockerfile untuk image OpenSSL, tools Kali, dan DNSMasq. |
| `01-sumber-lab/b/` | Berisi konfigurasi Docker Compose untuk pengujian multi-container, SYN Flood, dan DNS Exfiltration. |
| `01-sumber-lab/kasus/` | Berisi script Python untuk pengiriman ICMP dengan Scapy dan analisis log DNS. |
| `01-sumber-lab/k2-lab/` | Berisi file capture demo, script pembuat capture, dan wordlist untuk pengujian WPA2 Kasus 2. |
| `01-sumber-lab/samples/` | Berisi file referensi capture, wordlist, dan panduan sampel dari bank soal. |
| `02-dokumen/` | Berisi dokumen soal UTS, lembar perintah per kasus, dan checklist penguji. |
| `03-hasil kasus-2/` | Berisi dokumentasi hasil pengerjaan Kasus 2 dari Pertemuan 1 sampai 7. |
| `03-hasil kasus-2/jawaban.md` | Dokumentasi utama yang menggabungkan seluruh hasil Tugas 1–7. |
| `03-hasil kasus-2/tugas1/`–`tugas7/` | Dokumentasi terpisah untuk masing-masing tugas, termasuk screenshot. |
| `cleanup.sh` | Script pembersihan resource lab yang disediakan di repository. |

## Ringkasan Praktikum Pertemuan 1–7

| Pertemuan | Tugas | Materi | Ringkasan Hasil | Dokumentasi |
|---|---|---|---|---|
| 1 | Tugas 1 | Docker dan Volume | Volume `vol-k2` mempertahankan file NIM setelah container pembuat dihapus. Docker Compose juga berhasil menjalankan target Nginx dan attacker; halaman HTML Nginx berhasil diakses. | [`Tugas 1`](<03-hasil kasus-2/tugas1/hasil.md>) |
| 2 | Tugas 2 | Kriptografi | Enkripsi dan dekripsi AES-256-CBC berhasil. Hash SHA-256 plaintext dan hasil dekripsi sama. Sertifikat X.509 self-signed RSA 2048-bit berhasil dibuat dan diperiksa. | [`Tugas 2`](<03-hasil kasus-2/tugas2/hasil.md>) |
| 3 | Tugas 3 | ARP Spoofing | MAC Address gateway pada tabel ARP korban berubah menjadi MAC penyerang saat spoofing. Setelah mitigasi Static ARP, entri gateway kembali menggunakan MAC asli dan berstatus permanen. | [`Tugas 3`](<03-hasil kasus-2/tugas3/hasil.md>) |
| 4 | Tugas 4 | Analisis WPA2 Handshake | Capture awal diperiksa dan dinyatakan tidak layak dianalisis. Capture demo pengganti digunakan untuk menguji Aircrack-ng; kata sandi `k2network` ditemukan dari wordlist. | [`Tugas 4`](<03-hasil kasus-2/tugas4/hasil.md>) |
| 5 | Tugas 5 | ICMP dengan Scapy | Paket ICMP Echo Request dikirim dari `172.18.0.5` ke `172.18.0.2`. Balasan memiliki TTL 64 dan tipe ICMP 0 (Echo Reply). | [`Tugas 5`](<03-hasil kasus-2/tugas5/hasil.md>) |
| 6 | Tugas 6 | SYN Flood dan TCP Three-Way Handshake | Jumlah `SYN_RECV` yang teramati adalah 0 sebelum dan selama pengujian. Tcpdump memperlihatkan paket SYN, SYN-ACK, dan ACK pada koneksi HTTP normal. | [`Tugas 6`](<03-hasil kasus-2/tugas6/hasil.md>) |
| 7 | Tugas 7 | DNS Exfiltration | NIM dikonversi menjadi hexadecimal, dimasukkan sebagai label DNS query, log DNS dikumpulkan dan dianalisis, lalu data di-decode kembali menjadi NIM asli. | [`Tugas 7`](<03-hasil kasus-2/tugas7/hasil.md>) |

### Dokumentasi per tugas

- [Pertemuan 1 — Docker dan Volume](<03-hasil kasus-2/tugas1/hasil.md>)
- [Pertemuan 2 — Kriptografi](<03-hasil kasus-2/tugas2/hasil.md>)
- [Pertemuan 3 — ARP Spoofing](<03-hasil kasus-2/tugas3/hasil.md>)
- [Pertemuan 4 — Analisis Handshake WPA2](<03-hasil kasus-2/tugas4/hasil.md>)
- [Pertemuan 5 — ICMP dengan Scapy](<03-hasil kasus-2/tugas5/hasil.md>)
- [Pertemuan 6 — SYN Flood dan Three-Way Handshake](<03-hasil kasus-2/tugas6/hasil.md>)
- [Pertemuan 7 — DNS Exfiltration](<03-hasil kasus-2/tugas7/hasil.md>)

## Teknologi dan Tools

| Teknologi / Tools | Kegunaan dalam Praktikum |
|---|---|
| Windows PowerShell | Menjalankan perintah Docker dan mengelola file praktikum dari host Windows. |
| Docker Desktop | Menyediakan Docker Engine untuk menjalankan container pada Windows. |
| Docker | Menjalankan lingkungan laboratorium berbasis container. |
| Docker Compose | Mengelola beberapa container dan jaringan praktikum melalui file YAML. |
| Alpine Linux | Image ringan untuk pengujian volume dan layanan sederhana. |
| Nginx | Web server target untuk pengujian komunikasi HTTP. |
| OpenSSL | Enkripsi AES, dekripsi, hashing pendukung, serta pembuatan dan pemeriksaan sertifikat X.509. |
| RSA | Algoritma kunci publik yang digunakan pada pembuatan sertifikat. |
| Aircrack-ng | Analisis file capture dan pengujian WPA2 handshake secara offline. |
| Scapy | Membentuk, mengirim, dan menerima paket ICMP menggunakan Python. |
| hping3 | Membuat paket TCP SYN untuk simulasi SYN Flood di lab. |
| netstat | Mengamati status koneksi TCP, termasuk `SYN_RECV`. |
| tcpdump | Menangkap dan menganalisis paket jaringan. |
| dnsmasq | Menyediakan layanan DNS untuk simulasi DNS Exfiltration. |
| dig | Mengirim dan memeriksa DNS query. |
| xxd | Mengubah data teks menjadi hexadecimal dan sebaliknya. |
| Python 3 | Menjalankan script Scapy dan analisis log DNS. |

## Persiapan Lingkungan Praktikum

### Prasyarat

Sebelum menjalankan praktikum, pastikan perangkat telah memiliki:

1. Windows dengan PowerShell.
2. Docker Desktop yang sudah berjalan.
3. Docker Engine dan Docker Compose.
4. Koneksi internet saat proses build atau pull image.
5. Ruang penyimpanan yang cukup untuk Docker image dan file capture.

Periksa instalasi Docker:

```powershell
docker --version
docker compose version
```

### Build Docker Image

Masuk ke direktori source lab:

```powershell
cd 01-sumber-lab
```

Bangun image yang digunakan pada praktikum:

```powershell
docker build -t uts-openssl images/uts-openssl
docker build -t uts-kali-tools images/uts-kali-tools
docker build -t uts-dnsmasq images/uts-dnsmasq
```

### Unduh Image Pendukung

```powershell
docker pull alpine
docker pull nginx:alpine
docker pull vulnerables/web-dvwa
docker pull kalilinux/kali-rolling
```

Image perlu disiapkan sebelum menjalankan lab yang menggunakan jaringan Docker `internal: true`, karena jaringan internal tersebut tidak menyediakan akses internet langsung bagi container.

### Verifikasi Image

```powershell
docker image ls
```

Pastikan image yang dibutuhkan sudah tersedia sebelum memulai pengujian.

## Cara Menjalankan Praktikum

### 1. Buka Repository

Ekstrak repository, lalu buka folder `UTS-Network-Security` menggunakan VS Code.

### 2. Baca Dokumen Panduan

Pelajari dokumen berikut sebelum menjalankan perintah:

- [`02-dokumen/DOKUMEN-UTS-LENGKAP.md`](<02-dokumen/DOKUMEN-UTS-LENGKAP.md>)
- [`02-dokumen/LEMBAR-PERINTAH-PER-KASUS.md`](<02-dokumen/LEMBAR-PERINTAH-PER-KASUS.md>)
- [`01-sumber-lab/README.md`](<01-sumber-lab/README.md>)

### 3. Siapkan Image

Jalankan perintah build dan pull image sesuai bagian [Persiapan Lingkungan Praktikum](#persiapan-lingkungan-praktikum).

### 4. Jalankan Tugas Sesuai Pertemuan

Perintah praktikum menggunakan direktori kerja `01-sumber-lab` untuk konfigurasi yang berada di dalam folder tersebut. Periksa perintah dan parameter pada dokumentasi setiap tugas sebelum menjalankannya.

Ringkasan lokasi konfigurasi:

| Pertemuan | Lokasi File / Script Utama |
|---|---|
| 1 | `b/b1-compose/docker-compose.yml` dan Docker Volume |
| 2 | Image `uts-openssl` |
| 3 | Jaringan Docker `lab-arp-k2` dan tools `arpspoof` |
| 4 | `k2-lab/` dan file capture/wordlist WPA2 |
| 5 | `kasus/k5-scapy/kirim_icmp.py` |
| 6 | `b/b3-syn-flood/docker-compose.yml` |
| 7 | `b/b4-dns-exfil/docker-compose.yml` dan `kasus/k9-dns-detect/analisis_dns.py` |

### 5. Simpan Bukti Pengujian

Setiap tugas memiliki folder `screenshot/`. Simpan screenshot sesuai nomor urut yang digunakan dalam file `hasil.md`.

### 6. Bersihkan Resource Setelah Pengujian

Setelah setiap pengujian selesai, hentikan dan hapus container serta network yang dibuat oleh lab. Untuk layanan Docker Compose, perintah pembersihan yang digunakan dalam instruksi masing-masing tugas adalah:

```powershell
docker compose -p k2 -f b/b1-compose/docker-compose.yml down -v
```

Sesuaikan nama file Compose dengan tugas yang sedang dijalankan. Perhatikan bahwa opsi `-v` dapat menghapus volume yang dikelola oleh proyek Compose tersebut. Docker Volume terpisah yang dibuat manual perlu dikelola secara terpisah.

## Dokumentasi Hasil Pengerjaan

Dokumentasi lengkap seluruh tugas tersedia di:

**[`03-hasil kasus-2/jawaban.md`](<03-hasil kasus-2/jawaban.md>)**

Dokumentasi pendukung per tugas:

| Pertemuan | File Hasil | Folder Screenshot |
|---|---|---|
| 1 | [`tugas1/hasil.md`](<03-hasil kasus-2/tugas1/hasil.md>) | [`tugas1/screenshot/`](<03-hasil kasus-2/tugas1/screenshot/>) |
| 2 | [`tugas2/hasil.md`](<03-hasil kasus-2/tugas2/hasil.md>) | [`tugas2/screenshot/`](<03-hasil kasus-2/tugas2/screenshot/>) |
| 3 | [`tugas3/hasil.md`](<03-hasil kasus-2/tugas3/hasil.md>) | [`tugas3/screenshot/`](<03-hasil kasus-2/tugas3/screenshot/>) |
| 4 | [`tugas4/hasil.md`](<03-hasil kasus-2/tugas4/hasil.md>) | [`tugas4/screenshot/`](<03-hasil kasus-2/tugas4/screenshot/>) |
| 5 | [`tugas5/hasil.md`](<03-hasil kasus-2/tugas5/hasil.md>) | [`tugas5/screenshot/`](<03-hasil kasus-2/tugas5/screenshot/>) |
| 6 | [`tugas6/hasil.md`](<03-hasil kasus-2/tugas6/hasil.md>) | [`tugas6/screenshot/`](<03-hasil kasus-2/tugas6/screenshot/>) |
| 7 | [`tugas7/hasil.md`](<03-hasil kasus-2/tugas7/hasil.md>) | [`tugas7/screenshot/`](<03-hasil kasus-2/tugas7/screenshot/>) |

Setiap dokumentasi tugas memuat perintah yang digunakan, hasil pengujian, analisis, dan bukti screenshot yang relevan.

## Catatan Praktikum

1. Seluruh pengujian dilakukan pada lingkungan Docker lokal yang disiapkan untuk keperluan pembelajaran.
2. Perintah disesuaikan dengan lingkungan Windows PowerShell dan Docker Desktop.
3. Hasil laporan didasarkan pada output terminal dan screenshot yang tersedia dalam repository.
4. Hasil yang tidak muncul pada output tidak boleh dinyatakan berhasil tanpa bukti pendukung.
5. Pada Tugas 4, file capture awal diperiksa dan ditemukan tidak sesuai untuk analisis. Dokumentasi menjelaskan penggunaan capture demo pengganti; hasilnya perlu dibedakan dari capture asli yang disediakan.
6. Pada Tugas 6, jumlah `SYN_RECV` yang teramati adalah 0 sebelum dan selama pengujian. Nilai tersebut tidak dengan sendirinya membuktikan SYN Cookies aktif; status mekanisme tersebut memerlukan pemeriksaan parameter kernel secara langsung.
7. Pada Tugas 7, dokumentasi mencatat query DNS dan proses decoding NIM. Output analisis log yang terlihat tidak menampilkan baris query mencurigakan, sehingga hal tersebut tidak diklaim sebagai temuan yang terdeteksi.
8. Jangan menyimpan password, token, private key, atau data autentikasi yang masih berlaku ke repository publik. File `key-k2.pem` adalah private key hasil praktikum dan sebaiknya tidak dipublikasikan.
9. Seluruh simulasi serangan hanya boleh dilakukan pada jaringan laboratorium yang terisolasi dan telah memperoleh izin.

## Tujuan Repository

Repository ini dibuat untuk:

- Menyimpan source code, Dockerfile, konfigurasi, dan script pendukung praktikum.
- Menyediakan panduan persiapan serta pelaksanaan UTS praktik.
- Mendokumentasikan hasil pengerjaan Kasus 2 untuk Pertemuan 1 sampai 7.
- Menggabungkan hasil setiap tugas dalam satu dokumentasi utama `jawaban.md`.
- Menyimpan screenshot sebagai bukti pelaksanaan praktikum.
- Memudahkan dosen atau penguji dalam meninjau perintah, hasil, dan analisis setiap tugas.
- Menjadi arsip pembelajaran mengenai Docker, kriptografi, dan keamanan jaringan.

---

**Dokumentasi utama:** [`03-hasil kasus-2/jawaban.md`](<03-hasil kasus-2/jawaban.md>)  
**Kasus:** 2 (`k2`) — **Mata Kuliah:** Keamanan Jaringan (Security Network)
