FROM ruby:2.7.4

ENV LANG=C.UTF-8
ENV ENABLE_SERVICE_WORKER=true

WORKDIR /devdocs

RUN apt-get update && \
    apt-get -y install git nodejs libcurl4 && \
    gem install bundler

COPY Gemfile Gemfile.lock Rakefile /devdocs/

RUN bundle install --system && \
    rm -rf ~/.gem /root/.bundle/cache /usr/local/bundle/cache

COPY . /devdocs

EXPOSE 9292
CMD rackup -o 0.0.0.0
