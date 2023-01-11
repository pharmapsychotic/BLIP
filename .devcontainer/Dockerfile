FROM blip/jupyter:latest

WORKDIR /tmp

ARG USER_NAME=vscode
ARG USER_UID
ARG USER_GID
ARG DOCKER_GID

RUN groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
    && chmod 0440 /etc/sudoers.d/$USER_NAME \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

ENV SHELL=/usr/bin/zsh
RUN chsh $USER_NAME -s $SHELL

# Install dev dependences & tools
RUN apt update && apt install -y \
    htop \
    vim \
    git-lfs \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    ssh \
    rsync \
    kmod \
    sudo \
    make \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

# Install dev packages
COPY .devcontainer/requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt


RUN chown -R ${USER_NAME} /root

USER vscode
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
ENV PATH=$PATH:/home/vscode/.local/bin