 
docker network create appnet 2>/dev/null || true
 
docker rm -f backend frontend 2>/dev/null || true

docker run -d --name backend --network appnet -p 8000:8000 microservices/backend:1.0.0
docker run -d --name frontend --network appnet -p 8080:8080 \
  -e BACKEND_URL=http://backend:8000 microservices/frontend:1.0.0

echo "Containers started "
