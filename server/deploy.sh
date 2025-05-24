#!/bin/bash

# Nama stack
STACK_NAME=musicapp

# 1. Inisialisasi Docker Swarm jika belum
if ! docker info | grep -q "Swarm: active"; then
  echo "Initializing Docker Swarm..."
  docker swarm init
fi

# 2. Daftar secrets dan nilainya
declare -A secrets=(
  [cloudinary_api_key]="141551234981569"
  [cloudinary_api_secret]="3CAlZX7tC7--Sd3oce8L04HeDGE"
  [db_user]="admin"
  [db_password]="admin"
)

# 3. Hapus & buat ulang secrets
echo "Updating secrets..."
for key in "${!secrets[@]}"; do
  if docker secret ls | grep -q "$key"; then
    echo "  Removing old secret: $key"
    docker secret rm "$key"
  fi
  echo -n "${secrets[$key]}" | docker secret create "$key" -
done

# 4. Deploy stack
echo "Deploying stack '$STACK_NAME'..."
docker stack deploy -c docker-compose.prod.yml "$STACK_NAME"

# # Tunggu sebentar agar service bisa jalan dan container siap
# echo "Waiting 5 seconds for services to start..."
# sleep 2

# # Tampilkan logs dari service musicserver secara realtime (bisa di Ctrl+C untuk stop)
# echo "Showing logs for service ${STACK_NAME}_musicserver..."
# docker service logs -f "${STACK_NAME}_musicserver"

# 5. Tampilkan status
echo ""
docker stack services "$STACK_NAME"