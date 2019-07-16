FROM gitpod/workspace-full:latest

USER root
# Install custom tools, runtime, etc.
RUN apt-get install software-properties-common \
        && add-apt-repository -yu ppa:deadsnakes/ppa && apt-get update && apt-get install -y \
        python3.5 \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN apt-get update && apt-get install -y \
        postgresql \
        postgresql-contrib \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

USER gitpod
# Apply user-specific settings
#ENV ...

# Give back control
USER root