# Manual Deployment M03

## Application Path
`/srv/cc-m03`

## Service
`cc-m03.service` (systemd)

## Backend
Gunicorn pada `127.0.0.1:8000` (1 worker, 2 threads)

## Reverse Proxy
Caddy pada port 80, konfigurasi di `/etc/caddy/Caddyfile`

## Public Endpoint
`http://3.106.220.4/`

## Health Check
`GET /health` mengembalikan HTTP 200 dengan JSON `{"status":"ok"}`

## Update Procedure

```bash
cd /srv/cc-m03
git pull
source .venv/bin/activate
python -m pip install -r requirements.txt
sudo systemctl restart cc-m03
sudo systemctl status cc-m03 --no-pager
curl -fsS http://127.0.0.1:8000/health
curl -fsS http://127.0.0.1/health
```

Setelah itu, lakukan tes dari client eksternal.

## Logs

```bash
sudo journalctl -u cc-m03 -n 50 --no-pager
sudo journalctl -u caddy -n 50 --no-pager
```

## Rollback Dasar

```bash
git log --oneline --decorate -10
git checkout m03
sudo systemctl restart cc-m03
git switch main
```

## Catatan
- Deployment masih manual dan HTTP only (HTTPS pada M04).
- Tidak ada secret pada repository.
