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
                postgresql-client \
                nss_wrapper
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update -y \
    && apt-get install -y \
                python3.6 \
                python3.6-dev \
                python3.6-venv \
                python-psycopg2 \
                libpq-dev

# mara-app section - this is specific to our use of mara
# ======================================================

# Add mara user
ARG uid=1001
ARG user=mara
RUN useradd -U -ms /bin/bash -u $uid $user \
    && usermod -a -G root $user

ARG python_version=3.6

ENV HOME="/data-pipeline" \
    APP_ROOT="$HOME" \
    PYENV_ROOT="$HOME/.venv" \
    PATH=$PYENV_ROOT/bin:$PATH \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    SHELL=/bin/bash \
    PIP_NO_CACHE_DIR=off \
    PYTHON_VERSION="$python_version" \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 

LABEL io.k8s.display-name="mara" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="python,mara"

# Copy source code
ADD . $HOME
ADD ./docker/mara-app/docker-entrypoint.sh $HOME
ARG entrypoint="$HOME/docker-entrypoint.sh"

WORKDIR $HOME
RUN make install-packages

# Set ownership and permissions
# Set scripts as executable (make files and python files do not have to be marked)
RUN chown -R mara:root $HOME \
    && chmod -R ug+rw $HOME \
    && chmod ug+x $HOME/.scripts/mara-app/*.sh \
    && chmod ug+x $HOME/.scripts/mara-app/makeshell \
    && chmod ug+x $entrypoint

USER $uid
ENTRYPOINT ["bash", "docker-entrypoint.sh"]