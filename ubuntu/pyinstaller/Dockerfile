ARG PREFIX
ARG UBUNTU_VERSION
ARG PYTHON_VERSION

FROM ${PREFIX}ubuntu:${UBUNTU_VERSION}-python{$PYTHON_VERSION}

RUN apt-get update && apt-get install -y \
    bash \
    build-base \
    curl \
    freetype-dev \
    fribidi-dev \
    g++ \
    gfortran \
    git \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    libc-dev \
    libxml2-dev \
    libxslt-dev \
    libzmq \
    linux-headers \
    musl-dev \
    openblas-dev \
    openjpeg-dev \
    openssl \
    pkgconfig \
    postgresql-dev \
    pwgen \
    tcl-dev \
    tiff-dev \
    tk-dev \
    upx \
    zeromq-dev \
    zlib-dev


# Install poetry <3
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
    source $HOME/.poetry/env && \
    poetry config settings.virtualenvs.create false

VOLUME /src
WORKDIR /src
ADD ./bin /pyinstaller
RUN chmod a+x /pyinstaller/*

# Install requirements
ONBUILD COPY pyproject.* poetry.* requirements.* ./
ONBUILD RUN /pyinstaller/install_requirements.sh

ENTRYPOINT ["/pyinstaller/pyinstaller.sh"]
