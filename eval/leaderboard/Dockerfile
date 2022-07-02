FROM python:3.7

WORKDIR /app
RUN svn export https://github.com/google-research/google-research/trunk/rouge /app/rouge
RUN pip install -r /app/rouge/requirements.txt
RUN pip install transformers==4.18.0

COPY eval/automatic/evaluation.py /app/