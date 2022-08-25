############
#   base   #
############
FROM ubuntu:latest as base

ENV PATH ~/miniconda3/bin:$PATH
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y \
  build-essential \
  bzip2 \
  wget \
  cmake \
  git \
  gcc \
  vim \
  make && apt clean

ARG USERNAME=user
ARG GROUPNAME=user
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID $GROUPNAME && \
  useradd -m -s /bin/bash -u $UID -g $GID $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh -O ~/Miniconda.sh && \
  /bin/bash ~/Miniconda.sh -b -p ~/miniconda3 && \
  rm ~/Miniconda.sh && \
  echo ". ~/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc && \
  echo "conda activate base" >> ~/.bashrc

###########
#   dev   #
###########
FROM base as dev

# 開発に必要なパッケージをインストールする
# RUN conda install <hoge>
