# readme

```bash
docker build . -t knapiontek/traefik:latest
docker push knapiontek/traefik:latest
kubectl create deployment --image  knapiontek/traefik:latest mytraefik
kubectl expose deployment mytraefik --port=443 --type=LoadBalancer
kubectl expose deployment mytraefik --port=80 --type=LoadBalancer

kubectl scale deployment mytraefik --replicas=0
kubectl get pods
curl https://dev.knapiontek.com/
sudo apt-get install dnsmasq
```

```bash
docker build . -t knapiontek/traefik:v3
docker push knapiontek/traefik:v3

curl -u admin:skynet0iscoming -XGET https://admin.knapiontek.com/api/providers/rest | jq . > traefik.json
curl -u admin:skynet0iscoming -XPUT -d @traefik.json https://admin.knapiontek.com/api/providers/rest
```
