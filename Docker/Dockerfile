FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update -qq \
  && apt-get install -y --no-install-recommends python3 python3-pip git make ca-certificates libgomp1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/kevinywlui/langclass

WORKDIR "/langclass"

ENV PYTHONPATH /langclass

RUN pip3 install pipenv; pip3 install .; pipenv install

RUN make train

EXPOSE 5000
