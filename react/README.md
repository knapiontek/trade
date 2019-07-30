# readme

```bash
docker build . -t knapiontek/trade:latest
docker run --rm -p 3000:3000 -t knapiontek/trade:latest
docker push knapiontek/trade:latest
kubectl create deployment --image  knapiontek/trade:latest mytrade
```
