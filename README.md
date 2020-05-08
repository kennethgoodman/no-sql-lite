# no-sql-lite
A no sql lite database

# Setup
```bash
$ pip install -r requirements.txt
```

# Development setup

All of this uses python3, use python2 at your own risk

## setting up a virtual environment
```bash
$ virtualenv venv
$ source venv/bin/activate
```

## Set as dev mode
```bash
$ export PYTHONDEVMODE=1
```

If this is not set or not set to `"1"`, we will run in production mode

## Docker 

install docker to test in production-like environment: 
https://www.docker.com/

### commands:

#### Starting Server
```bash
$ bash ./start.sh
```

#### Restarting Server

##### TODO(kgoodman) DOESNT WORK RIGHT NOW
```bash
$ touch uwsgi.ini
```

#### Storing Data
```bash
$ curl  -X PUT \
        -H "Content-Type: application/json" \
        --data '{"key":"abcd","data":{"a":"b"}}' \
        localhost:56733/write_data
```

#### Fetching Data
```bash
$ curl -X GET "localhost:56733/get_data?key=abcd"
```

#### Seeing Logs
```bash
$ docker logs no_sql_lite
```

#### SSH To Docker 
```bash
$ docker exec -it no_sql_lite /bin/bash
```

## Web pages
1. [Index Page](http://localhost:56733/)
2. [Get Data](http://localhost:56733/get_data_page)

# Running
```bash
$ python main.py
```
