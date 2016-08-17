FROM debian:jessie

ENV DEBIAN_FRONTEND=noninteractive 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y -q python3-pip 

ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt
ADD ./webapp /opt/webapp/

WORKDIR /opt/webapp
EXPOSE 5000

# Bind listen iface by running flask instead of app.py to keep code without network config
ENV FLASK_APP=app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

