# samesite-demo
Flask app to demonstrate SameSite cookie behaviour

## Local Setup
```
python app.py
```

## Podman/Docker Setup
```
podman build -t samesite-demo .
podman run -d -p 8181:8181 --name samesite_demo samesite-demo
```