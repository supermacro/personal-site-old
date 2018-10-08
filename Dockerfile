FROM giorgio14/pelican:0.1.0

WORKDIR /blog

COPY content content/
COPY plugins plugins/
COPY theme theme/
COPY Makefile .
COPY jinjafilters.py ./jinjafilters.py
COPY pelicanconf.py ./pelicanconf.py
COPY publishconf.py /publishconf.py
COPY develop_server.sh ./develop_server.sh

EXPOSE 8080:8080

CMD ["make", "devserver", "PORT=8080"]
