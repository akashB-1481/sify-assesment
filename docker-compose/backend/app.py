from flask import Flask , jsonify
import redis    
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")
redis_password = os.getenv("REDIS_PASSWORD")
r = redis.Redis(host=redis_host, port=6379 , password=redis_password , decode_responses=True)

@app.route("/")
def home():
    return jsonify({"message": "Backend running"})

@app.route("/api")
def api():
    count = r.incr("hits")
    return jsonify({"hits": count})

@app.route("/health")
def health():
    try:
        r.ping()
        return {"status": "ok"}, 200
    except:
        return {"status": "fail"}, 500    

if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=5000)        