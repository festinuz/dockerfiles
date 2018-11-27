ARG PREFIX
ARG UBUNTU_VERSION
ARG PYTHON_VERSION

FROM ${PREFIX}ubuntu:${UBUNTU_VERSION}-python$PYTHON_VERSION

RUN apt-get update && apt-get install -y \
    bash \
    curl \
    g++ \
    gfortran \
    git \
    libc-dev \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
    openssl \
    pwgen \
    tcl-dev \
    tk-dev \
    upx


# Install poetry <3
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
# Add poetry to path
ENV PATH="/root/.poetry/bin:$PATH"
# Config poetry
RUN poetry config settings.virtualenvs.create false


VOLUME /src
WORKDIR /src
ADD ./bin /pyinstaller
RUN chmod a+x /pyinstaller/*

# Install requirements
ONBUILD COPY pyproject.* poetry.* requirements.* ./
ONBUILD RUN /pyinstaller/install_requirements.sh

ENTRYPOINT ["/pyinstaller/pyinstaller.sh"]
