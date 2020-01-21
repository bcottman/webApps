FROM python:3.7
WORKDIR /dataViewer
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python dataViewer4.py