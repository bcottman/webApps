# supporting command
$ docker build -f Dockerfile -t helloworld-streamlit:latest .

#  runs in background

$ docker run -p 8501:8501 helloworld-streamlit &  