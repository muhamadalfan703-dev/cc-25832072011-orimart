# OriMart

Cloud Computing — PTI 2802
Pertemuan 3 — Project Inception

## Author
Muhamad Alfan Maulana — NIM 25832072011

## Problem
Pembeli pakaian, sepatu, dan tas/aksesoris fashion bekas bermerek (thrift)
kesulitan memastikan keaslian barang yang dibeli secara online.
OriMart menyediakan katalog thrift fashion bermerek dengan lencana "Ori"
yang menandai barang lolos pemeriksaan bukti sesuai checklist verifikasi.

## Target Users
- Pembeli thrift fashion bermerek
- Admin/penjual yang menampilkan produk terverifikasi

## Features M03
- Halaman utama dengan kategori dan contoh produk (data statis)
- Lencana "Ori" beserta catatan bahwa lencana bukan jaminan mutlak
- Health endpoint (`GET /health`)
- Deployment pertama pada VPS

## Architecture

```mermaid
flowchart LR
    U[User] --> F[UFW]
    F --> C[Caddy :80]
    C --> G[Gunicorn 127.0.0.1:8000]
    G --> A[Flask]
```

## Infrastructure
- Ubuntu Server 24.04 LTS
- Target desain: 1 vCPU, 1 GB RAM, 20 GB disk (instance AWS aktual: 2 vCPU, sekitar 1 GB RAM)
- Flask, Gunicorn (1 worker, 2 threads), systemd, Caddy, UFW

## Public Endpoint
`http://3.106.220.4/`

## Health Check
`GET /health` mengembalikan HTTP 200 dengan JSON `{"status":"ok"}`

## Deployment
Lihat `docs/deployment.md`.

## Documentation
- `docs/requirements.md`
- `docs/architecture.md`
- `docs/adr/0001-initial-architecture.md`
- `docs/deployment.md`
- `docs/evidence/m03/`

## Security
- SSH key-only, root login dinonaktifkan
- UFW aktif (hanya port 22 dan 80)
- Backend hanya listen pada loopback
- Tidak ada secret pada repository

## Current Limitations
- HTTP only (HTTPS pada M04)
- Data contoh statis, belum ada database
- Belum menggunakan container
- Deployment manual

## Roadmap
M04 DNS/HTTPS, M05 Data, M06 Container, M07 IaC, M09 CI/CD
