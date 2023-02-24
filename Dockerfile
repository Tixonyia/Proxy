FROM ubuntu
RUN apt-get update \
 && apt-get install -y \
    python3 \
    python3-pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ENV INSTALL_PATH /docker-flowcell-restore
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

ENV PORT=50013

EXPOSE 50013

RUN pip install -r requirements.txt

COPY src/ src/

ENTRYPOINT ['python', 'src/main.py']