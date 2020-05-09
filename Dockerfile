FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN apt-get update && apt-get install -y nmap vim
COPY ./app /app
COPY uwsgi.ini /app/uwsgi.ini
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt