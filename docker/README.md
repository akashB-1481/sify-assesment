### 🔹 docker compose build

```bash
 docker-compose up --build
```

### 🔹 Output

```
Name              Command          State    Ports
------------------------------------------------
nginx             nginx -g ...     Up       0.0.0.0:8080->80/tcp
backend           python app.py    Up
redis             docker-entry...  Up
```


### 🔹 Check running containers

```bash
docker-compose ps
```

### 🔹 Output

```
Name              Command          State    Ports
------------------------------------------------
nginx             nginx -g ...     Up       0.0.0.0:8080->80/tcp
backend           python app.py    Up
redis             docker-entry...  Up
```