ARG VERSION

FROM ubuntu:$VERSION


# Install dumb-init (https://github.com/Yelp/dumb-init)
RUN apt-get update && \
    apt-get install -y wget && \
    wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && \
    chmod a+x /usr/local/bin/dumb-init
