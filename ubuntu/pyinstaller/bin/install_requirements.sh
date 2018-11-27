#!/bin/sh

if [ -f requirements.txt ]; then
    echo "requirements.txt file found; Installing dependencies with pip"
    pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
elif [ -f setup.py ]; then
    echo "setup.py file found; Installing dependencies with pip"
    pip install --no-cache-dir --disable-pip-version-check .
elif [ -f poetry.lock ]; then
    echo "poetry.lock file found; Installing dependencies using poetry"
    poetry install --no-dev --no-interaction
elif [ -f pyproject.toml ]; then
    echo "pyproject.toml file found; Trying to install dependencies using poetry"
    poetry install --no-dev --no-interaction
else
    echo "No file specifying requirements found; No dependencies are installed"
fi


echo "Installing PyInstaller & pycrypto"
git clone --depth 1 --single-branch --branch=v3.4 https://github.com/pyinstaller/pyinstaller.git /tmp/pyinstaller \
    && cd /tmp/pyinstaller/bootloader \
    && python ./waf configure --no-lsb all \
    && pip install .. \
    && cd ~ \
    && rm -Rf /tmp/pyinstaller \
    && pip install --no-cache-dir --disable-pip-version-check pycrypto
