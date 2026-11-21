#!/usr/bin/env bash
# Test the services with curl 🔍
sleep 2

for url in localhost:8000/health localhost:8000/info localhost:8080/health localhost:8080/info; do
  echo "curl $url"
  curl -s $url
  echo
done

# Check that the containers do NOT run as root (should show uid=1001)
echo "--- user check ---"
docker exec backend id
docker exec frontend id
