### 🔹 docker compose build

```bash
 cmd
```

### 🔹 Output

```
output
```

### 🔹 Check running containers

```bash
docker-compose ps
```

### 🔹 Output

```
akashb1408@ip-172-18-5-9:~/sify-assesment/sify-assesment/docker$ docker-compose ps
      Name                     Command               State                  Ports
-------------------------------------------------------------------------------------------------
docker_backend_1    python app.py                    Up
docker_frontend_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:8080->80/tcp,:::8080->80/tcp
docker_redis_1      docker-entrypoint.sh redis ...   Up      6379/tcp
akashb1408@ip-172-18-5-9:~/sify-assesment/sify-assesment/docker$

```

### 🔹 curl output nginx

```bash
 curl localhost:8080
```

### 🔹 Output

```
<!doctype html>
<html>
  <head>
    <title>K8s Assignment App</title>
  </head>
  <body>
    <h1>Welcome to My App 🚀</h1>
    <p>This is served by Nginx</p>

    <button onclick="getData()">Call Backend API</button>

    <p id="output"></p>

    <script>
      function getData() {
        fetch("/api")
          .then((response) => response.json())
          .then((data) => {
            document.getElementById("output").innerText = "Hits: " + data.hits;
          });
      }
    </script>
  </body>
</html>

```

### 🔹 curl output flask

```bash
 curl localhost:8080/api
```

### 🔹 Output

```
{"hits":1}


{"hits":2}

{"hits":3}

```

### Archietecture

Client (Browser / curl)
↓
Nginx (Port 8080)
↓
Flask API (Port 5000)
↓
Redis (Port 6379)

### 🔹 ping output

### Frontend (Nginx) to Backend (Pyhton) & to DB (Redis )

```bash
  docker exec -it docker_frontend_1 ping docker_backend_1 -c4

  docker exec -it docker_frontend_1 ping docker_redis_1 -c4
```

### 🔹 Output

```
PING docker_backend_1 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=0.337 ms
64 bytes from 172.19.0.3: seq=1 ttl=64 time=0.157 ms
64 bytes from 172.19.0.3: seq=2 ttl=64 time=0.059 ms
64 bytes from 172.19.0.3: seq=3 ttl=64 time=0.065 ms

--- docker_backend_1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.059/0.154/0.337 ms

```

```

PING docker_redis_1 (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: seq=0 ttl=64 time=0.083 ms
64 bytes from 172.19.0.2: seq=1 ttl=64 time=0.067 ms
64 bytes from 172.19.0.2: seq=2 ttl=64 time=0.063 ms
64 bytes from 172.19.0.2: seq=3 ttl=64 time=0.062 ms

--- docker_redis_1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.062/0.068/0.083 ms

```
