ARG UBUNTU_VERSION

FROM ubuntu:$UBUNTU_VERSION

ARG PYTHON_VERSION


# Install pyenv & python build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    llvm \
    make \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev

# Install pyenv and required python version
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash && \
    export PATH="/root/.pyenv/bin:$PATH" && \
    pyenv install $PYTHON_VERSION && \
    pyenv global $PYTHON_VERSION
