FROM ruby:2.7.4

ENV LANG=C.UTF-8
ENV ENABLE_SERVICE_WORKER=true

WORKDIR /

RUN git config --global http.proxy http://192.168.253.1:7890

RUN export http_proxy=192.168.253.1:7890
RUN export https_proxy=192.168.253.1:7890

RUN git clone https://github.com/vertexi/devdocs.git

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs libcurl4 && \
    gem install bundler

RUN bundle install --system && \
    rm -rf ~/.gem /root/.bundle/cache /usr/local/bundle/cache

RUN apt update && \
    apt install -y vim zsh tmux

EXPOSE 9292
CMD rackup -o 0.0.0.0

