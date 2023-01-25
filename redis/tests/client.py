import redis

# r=redis.Redis(password='egr',host='l201',port=6379,decode_responses=True)
r=redis.Redis(password='egr',host='127.0.0.1',port=6379,decode_responses=True)
# r=redis.Redis(host='redis',port=6379,decode_responses=True)
q=r.set('foo',20)
print(q)
v=r.get('foo')
print(v)
r.close()
