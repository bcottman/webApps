# supporting command
$ docker build -f Dockerfile -t dataviewer-flask:latest .

#  runs in background

$ docker run -pd 5000:5000 dataviewer-flask &  