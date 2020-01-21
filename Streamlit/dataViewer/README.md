# supporting command
$ docker build -f Dockerfile -t dataviewer-streamlit:latest .

#  runs in background

$ docker run -p 8501:8501 dataviewer-streamlit &  