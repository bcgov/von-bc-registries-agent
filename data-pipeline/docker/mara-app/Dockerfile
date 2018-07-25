FROM ubuntu:16.04

# marabase section

RUN apt-get update -y && apt-get install -y \
  build-essential \
  git dialog coreutils graphviz \
  software-properties-common python-software-properties \
        postgresql-client
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y && apt-get install -y \
  python3.6 python3.6-dev python3.6-venv \
  python-psycopg2 libpq-dev

# mara app section - this is specific to our use of mara

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD . /data-pipeline
RUN chown -R 1001:0 "/data-pipeline" \
    && chmod -R ug+rw "/data-pipeline" \
    && chmod ug+x "/data-pipeline/.scripts/*.sh" \
    && chmod ug+x "/data-pipeline/.scripts/makeshell"

# Debugging
RUN pwd
RUN ls -last
RUN cd data-pipeline/ \
    && ls -last .scripts/mara-app \
    && make install-packages

