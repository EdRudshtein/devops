import redis

#host='10.0.0.201'
host='127.0.0.1'
r=redis.Redis(host=host, port=6379)
r.mset({"Croatia":"Zagreb", "Bahamas":"Nassau"})
s=r.get("Bahamas")
print(s)
print(r.ping())
