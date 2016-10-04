FROM python:latest

EXPOSE 8080

RUN mkdir -p /src/www

COPY web.py /src
COPY index.html /src/www

CMD cd /src/www; /bin/bash -c 'python3 -u /src/web.py'

