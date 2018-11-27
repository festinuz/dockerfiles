ARG PREFIX
ARG VERSION

FROM ${PREFIX}ubuntu:$VERSION



# Install xvfb and basic libs
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    xvfb


# Set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


# Install google chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable


# Install chromedriver  (http://chromedriver.chromium.org/downloads)
COPY match_chromedriver_version /usr/local/bin/match_chromedriver_version
RUN CHROME_VERSION=`google-chrome-stable --version` && \
    CHROMEDRIVER_VERSION=`match_chromedriver_version "$CHROME_VERSION"` && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
    chmod a+x /usr/local/bin/chromedriver
