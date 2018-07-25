FROM ubuntu:16.04

# mara-base section
RUN apt-get update -y \
    && apt-get install -y \
                build-essential \
                git \
                dialog \
                coreutils \
                graphviz \
                software-properties-common \
                python-software-properties \
                postgresql-client
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y \
    && apt-get install -y \
                python3.6 \
                python3.6-dev \
                python3.6-venv \
                python-psycopg2 \
                libpq-dev

# mara-app section - this is specific to our use of mara
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Copy source code
ADD . /data-pipeline

# Set ownership and permissions
# Set scripts as executable (make files and python files do not have to be marked)
RUN chown -R 1001:0 /data-pipeline \
    && chmod -R ug+rw /data-pipeline \
    && chmod ug+x /data-pipeline/.scripts/mara-app/*.sh \
    && chmod ug+x /data-pipeline/.scripts/mara-app/makeshell

RUN cd data-pipeline/ \
    && make install-packages

