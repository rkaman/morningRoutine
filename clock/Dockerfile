FROM resin/rpi-raspbian:latest

RUN apt-get -y update && \
    apt-get install python3 python3-pip

COPY . /clock

RUN pip3 install -r /clock/REQUIREMENTS.txt

CMD ["python3", "/clock/clock.py"]