# Networking — M04

## VPS

- Provider: AWS (EC2), Ubuntu Server 24.04.5 LTS
- Public IPv4: `3.106.220.4` (dipetakan provider; tidak muncul pada `ip addr`)
- Private IPv4: `172.31.28.10/20`

## Interface

- Interface utama: `ens5`
- Loopback: `lo` (`127.0.0.1`)

## Default Route

`default via 172.31.16.1 dev ens5`

## IPv6

Tidak ada alamat IPv6 global (hanya link-local `fe80::` pada `ens5`).
Karena itu AAAA record **tidak** dibuat.

## DNS

Belum dikonfigurasi. Menunggu domain/subdomain (ditunda atas arahan dosen).
Rencana: A record `<DOMAIN>` -> `3.106.220.4`.

## Public Ports (kondisi saat ini)

| Port | Protocol | Purpose |
|---:|---|---|
| 22 | TCP | SSH administration |
| 80 | TCP | HTTP (Caddy) |

Rencana setelah domain tersedia: tambah 443/tcp untuk HTTPS.

## Internal Ports

| Address | Port | Service |
|---|---:|---|
| 127.0.0.1 | 8000 | Gunicorn |
| 127.0.0.1 | 2019 | Caddy admin API |

## Firewalls

- Provider firewall: AWS Security Group
- Host firewall: UFW (default deny incoming; allow 22, 80)

## Evidence

`docs/evidence/m04/network-baseline.txt`
