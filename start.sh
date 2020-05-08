#!/bin/bash
app="no_sql_lite"
docker build -t ${app} .
docker run -d -p 56733:80 --name=${app} ${app}