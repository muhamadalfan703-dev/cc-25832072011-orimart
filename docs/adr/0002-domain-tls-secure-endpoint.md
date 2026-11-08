# ADR-0002: Public DNS and TLS Termination with Caddy

## Status
Proposed (menunggu domain/subdomain; akan menjadi Accepted setelah HTTPS aktif)

## Context

M03 menggunakan public IPv4 dan HTTP pada port 80.
M04 membutuhkan hostname stabil dan secure endpoint.
VPS: AWS EC2, Ubuntu Server 24.04, 2 vCPU (hasil nproc), sekitar 1 GB RAM,
20 GB disk. Tidak ada IPv6 publik (hanya link-local).
Security Group saat ini hanya mengizinkan TCP 22 dan 80.

## Decision

- gunakan subdomain publik (menunggu dari dosen);
- gunakan A record ke public IPv4 VPS;
- jangan membuat AAAA karena VPS tidak memiliki IPv6 publik;
- gunakan Caddy sebagai TLS terminator dan reverse proxy;
- pertahankan Gunicorn pada 127.0.0.1:8000;
- buka TCP/443 pada UFW dan Security Group (TCP/80 tetap terbuka);
- gunakan automatic HTTPS bawaan Caddy.

## Alternatives Considered

1. NGINX + Certbot
2. Apache + Certbot
3. Aplikasi melayani TLS langsung
4. Self-signed certificate
5. Akses berbasis IP tanpa domain

## Rationale

- Caddy sudah terpasang dan menjadi reverse proxy sejak M03.
- Automatic HTTPS menghapus kebutuhan cron renewal terpisah.
- Footprint kecil, sesuai RAM 1 GB.
- Pemisahan tanggung jawab tetap jelas: Caddy menangani TLS,
  Gunicorn menjalankan aplikasi.
- Self-signed tidak dipercaya browser; akses via IP tidak bisa
  mendapat certificate publik.

## Consequences

### Positive
- HTTPS publik yang valid;
- lifecycle certificate otomatis;
- aplikasi tetap sederhana;
- backend tetap tidak diekspos.

### Negative
- bergantung pada DNS yang benar;
- bergantung pada ketersediaan CA/ACME;
- port 80 dan 443 harus reachable untuk challenge default.

## Risks

- DNS salah atau AAAA stale;
- Security Group menutup 80/443;
- IP publik berubah jika instance di-stop tanpa Elastic IP;
- rate limit ACME jika eksperimen berulang tidak terkontrol;
- SSH (port 22) terbuka untuk 0.0.0.0/0, dimitigasi dengan key-only.

## Review Trigger

Tinjau jika pindah provider, menambah load balancer/CDN,
mengadopsi container, atau membutuhkan wildcard certificate.
