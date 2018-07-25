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

RUN git clone https://github.com/ianco/von-bc-registries-agent.git
RUN mv /von-bc-registries-agent/data-pipeline /

# Debugging
RUN ls -last .scripts/mara-app

RUN cd data-pipeline/ && make install-packages

