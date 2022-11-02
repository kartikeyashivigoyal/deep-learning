ARGS VERSION=
ARGS FROM=
FROM $FROM

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get clean && \
    apt-get update --fix-missing && apt-get install -y
