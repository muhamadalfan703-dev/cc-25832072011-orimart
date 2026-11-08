# ADR-0001: Initial Deployment Architecture OriMart

## Status

Accepted

## Context

OriMart adalah marketplace thrift fashion bermerek dengan verifikasi
keaslian produk. Server menggunakan Ubuntu Server 24.04 LTS dengan
1 vCPU, RAM 1 GB, dan disk 20 GB. Proyek bersifat individual dan
berkembang secara iteratif sampai pertemuan 16.

## Decision

- Flask sebagai framework aplikasi web
- Gunicorn dengan 1 worker sebagai application server (bind 127.0.0.1:8000)
- systemd sebagai pengelola service
- Caddy sebagai reverse proxy
- UFW sebagai firewall host
- GitHub sebagai repository dan single source of truth

## Alternatives

1. Node.js + PM2
2. NGINX + Gunicorn
3. Docker
4. PHP-FPM

## Rationale

Python 3.12 sudah menjadi runtime default pada Ubuntu 24.04. Stack ini
ringan sehingga sesuai dengan RAM 1 GB. Gunicorn hanya listen pada
loopback agar backend tidak terekspos langsung ke internet, dan Caddy
menjadi satu-satunya pintu masuk publik. Caddy sederhana dan siap
dikembangkan ke HTTPS pada M04. Docker ditunda karena containerization
dipelajari pada M06.

## Consequences

### Positive

- Ringan dan mudah dipahami
- Backend tidak terekspos langsung ke internet
- Service otomatis hidup kembali setelah reboot

### Negative

- 1 worker membatasi jumlah request bersamaan
- Deployment masih manual
- Masih HTTP sampai M04

## Review Trigger

Review pada M06/M07.
