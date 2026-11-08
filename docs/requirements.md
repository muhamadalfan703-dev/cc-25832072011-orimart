# Requirements - OriMart

## Problem Statement

Pembeli barang thrift fashion bermerek mengalami kesulitan memastikan
keaslian barang dan kondisinya pada marketplace online umum.

OriMart menyediakan katalog barang thrift fashion bermerek yang setiap
produknya diverifikasi keasliannya oleh admin berdasarkan foto bukti
dari penjual, sehingga pembeli dapat membeli dengan yakin dan penjual
jujur mendapat kepercayaan serta pasar yang lebih luas.

## Target Users

- Pembeli: mencari dan membeli barang thrift bermerek yang asli.
- Penjual: menjual barang thrift dan mengajukan verifikasi produk.
- Admin: memeriksa bukti produk dan menangani laporan barang palsu.

## User Needs

- Sebagai pembeli, saya ingin melihat lencana "Ori" beserta foto bukti
  dan kondisi barang, sehingga saya yakin barang thrift itu asli.
- Sebagai penjual, saya ingin mengajukan produk untuk diverifikasi,
  sehingga produk saya dipercaya dan lebih cepat laku.
- Sebagai admin, saya ingin memeriksa bukti produk dan menandai hasilnya
  (lolos atau ditolak), sehingga hanya barang yang meyakinkan yang
  mendapat lencana "Ori".

## Value for Both Sides

- Pengguna: aman dari barang palsu dan mendapat informasi kondisi barang
  yang transparan.
- Pemilik platform: reputasi sebagai thrift terpercaya, dengan potensi
  pendapatan dari biaya verifikasi atau komisi penjualan.

## Scope Kategori

Fokus pada thrift fashion bermerek (pakaian, sepatu, tas/aksesoris
fashion), karena keasliannya dapat diperiksa melalui foto atau video
(tag, label, jahitan, kode produk). Kategori lain seperti elektronik
tidak termasuk karena sulit dibuktikan lewat foto.

## Definisi Lencana "Ori"

Lencana "Ori" berarti produk lolos pemeriksaan bukti sesuai checklist
verifikasi. Lencana ini bukan jaminan mutlak.

## Functional Requirements

Target M03:

- FR-01 Sistem menampilkan halaman utama OriMart (nama, tagline, kategori).
- FR-02 Sistem menyediakan endpoint /health yang mengembalikan HTTP 200.
- FR-03 Sistem menampilkan metadata aplikasi (nama, versi, status).
- FR-04 Sistem menampilkan daftar contoh produk thrift beserta lencana
  "Ori" dan kondisi barang (data statis).

Rencana milestone berikutnya:

- FR-05 Penjual dapat mendaftar dan login.
- FR-06 Penjual dapat mengunggah produk beserta foto bukti.
- FR-07 Admin dapat memeriksa bukti dan menandai produk lolos atau ditolak.
- FR-08 Pembeli dapat mencari dan memfilter produk berdasarkan kategori,
  merek, dan kondisi.
- FR-09 Pembeli dapat melaporkan produk yang diduga palsu.

## Non-Functional Requirements

- NFR-01 Backend hanya listen pada loopback (127.0.0.1:8000).
- NFR-02 Aplikasi dikelola systemd dan hidup kembali setelah reboot.
- NFR-03 Request publik masuk melalui reverse proxy (Caddy).
- NFR-04 Secret tidak disimpan pada Git repository.
- NFR-05 Health endpoint mengembalikan HTTP 200 saat sehat.
- NFR-06 Deployment dapat direproduksi dari repository.
- NFR-07 Arsitektur sesuai server 1 vCPU / 1 GB RAM.

## Scope M03

In scope:

- repository, requirements, architecture, dan ADR
- aplikasi Flask dasar dengan halaman OriMart
- hardening SSH dasar
- Gunicorn, systemd, dan Caddy
- deployment HTTP publik

Out of scope:

- database
- login dan upload foto
- panel admin
- Docker, CI/CD, domain, dan HTTPS

## Constraints

- Ubuntu Server 24.04 LTS
- 1 vCPU
- 1 GB RAM
- 20 GB disk
- public IPv4

## Acceptance Criteria M03

- [ ] first deployment dapat diakses melalui http://PUBLIC_IP/
- [ ] health endpoint /health mengembalikan HTTP 200
- [ ] backend hanya listen pada loopback
- [ ] aplikasi berjalan sebagai service systemd
- [ ] UFW aktif dan SSH hanya dengan key
