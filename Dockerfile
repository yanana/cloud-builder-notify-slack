FROM python:3.6

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yqq cmake && apt-get clean && \
  cd /tmp && \
  wget https://github.com/libgit2/libgit2/archive/v0.25.1.tar.gz && \
  tar xzf v0.25.1.tar.gz && \
  cd libgit2-0.25.1/ && \
  cmake . && \
  make && \
  make install && \
  cd .. && \
  pip install pygit2 requests && \
  rm -rf libgit2-0.25.1

COPY notify.py /usr/local/bin/
ENV LD_LIBRARY_PATH /usr/local/lib

ENTRYPOINT ["/usr/local/bin/notify.py"]
