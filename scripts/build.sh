 
set -e
cd "$(dirname "$0")/.."

docker build -t microservices/backend:1.0.0 services/backend
docker build -t microservices/frontend:1.0.0 services/frontend

echo "Images built  "
docker images | grep microservices
