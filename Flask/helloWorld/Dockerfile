FROM python:3.7
WORKDIR /helloWorld
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python helloWorld.py