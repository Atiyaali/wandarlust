#!/bin/bash
set -e 
cd ~/wandarlust 
echo "VERSION=${VERSION}" > .env 
docker compose down || true
docker compose pull 
docker compose up -d 
echo "deployment successfull"

