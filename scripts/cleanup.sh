
docker rm -f backend frontend 2>/dev/null
docker network rm appnet 2>/dev/null
echo "Cleaned up  "
