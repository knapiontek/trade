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
```
