 
sleep 2

for url in localhost:8000/health localhost:8000/info localhost:8080/health localhost:8080/info; do
  echo "curl $url"
  curl -s $url
  echo
done

 
echo "--- user check ---"
docker exec backend id
docker exec frontend id
