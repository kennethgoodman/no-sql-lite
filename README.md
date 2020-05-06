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

## install wsgi

I am using mod_wsgi-httpd to avoid using the default apache version as per:
https://github.com/GrahamDumpleton/mod_wsgi/issues/357
```bash
$ CC=cc pip install mod_wsgi-httpd --no-cache-dir -v
```

This step may take a couple minutes

## Set as dev mode
```bash
$ export PYTHONDEVMODE=1
```

If this is not set or not set to `"1"`, we will run in production mode

## Mac OS Mojave Apache
```base
$ apachectl start
```

# Running
```bash
$ python src/main.py
```
