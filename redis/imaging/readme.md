# Redis 

## Docker 

Docker image [here](https://hub.docker.com/_/redis)

## Set up

Set up volume ([documentation](https://redis.io/topics/persistence)) and network ([documentation [TODO]](https://www.google.com))
```
docker volume create redis
docker network create redis
```

## Launch Redis

Start Redis (v6.2) with custom config
### Command (PowerShell Core)
```
docker run -d -it --rm `
    --name redis `
    --net redis `
    -v ${PWD}/config:/etc/redis `
    -v redis:/data/ `
    -p 6379:6379 `
    redis:6.2-alpine `
    redis-server /etc/redis/redis.conf
```

Redis configuration [documentation](https://redis.io/topics/config)


## Security

Redis should not be exposed to public.
Always use a strong password in `redis.conf`

```
requirepass <mypassword>
```

# Redis Client

An example application that reads a key from Redis, increments it and writes it back to Redis.

```
TODO
```

Run our application

```
TODO
```

# Redis Replication and High Availability

Lets move on to the [clustering](./clustering/readme.md) secion.