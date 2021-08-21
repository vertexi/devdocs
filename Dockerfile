FROM ruby:2.7.4

ENV LANG=C.UTF-8
ENV ENABLE_SERVICE_WORKER=true

ARG proxy_addr

WORKDIR /

RUN git config --global http.proxy $proxy_addr

RUN echo 'Acquire::http::Proxy "$proxy_addr";' > /etc/apt/apt.conf

RUN export http_proxy=$proxy_addr
RUN export https_proxy=$proxy_addr

RUN git clone https://github.com/vertexi/devdocs.git

WORKDIR /root

RUN mkdir temp

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs libcurl4 && \
    gem install bundler

RUN bundle install --system && \
    rm -rf ~/.gem /root/.bundle/cache /usr/local/bundle/cache

RUN apt-get update && \
    apt-get install -y vim zsh tmux universal-ctags

RUN printf 'set nocompatible\n\
filetype plugin indent on\n\
syntax on\n\
set autoindent\n\
set expandtab\n\
set softtabstop =4\n\
set shiftwidth  =4\n\
set laststatus  =2\n\
set incsearch\n\
set hlsearch\n\
set cursorline\n\
set relativenumber\n' > /root/.vimrc

RUN printf 'export http_proxy=$proxy_addr\n\
export https_proxy=$proxy_addr\n' > /root/.bashrc

EXPOSE 9292
