FROM python:3.7

RUN apt update && apt install -y sudo
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
RUN sudo apt -y install nodejs   
RUN pip3 install Jinja2 pyyaml

COPY app/ /app/
RUN cd /app && npm install

COPY template/ /template/
COPY script.py /script.py
COPY entrypoint.sh .

ENTRYPOINT [ "/bin/sh","/entrypoint.sh" ]
