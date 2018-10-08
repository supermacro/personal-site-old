FROM ruby:2.5

WORKDIR /blog

COPY content content/
COPY plugins plugins/
COPY theme theme/
COPY Makefile .
COPY jinjafilters.py ./jinjafilters.py
COPY pelicanconf.py ./pelicanconf.py
COPY publishconf.py /publishconf.py
COPY requirements.txt ./requirements.txt
COPY develop_server.sh ./develop_server.sh

RUN apt-get update && apt-get install -y apt-utils python python-pip && \
    pip install -r requirements.txt && \
    gem install sass

# && make html


EXPOSE 8080:8080

CMD ["make", "devserver", "PORT=8080"]
