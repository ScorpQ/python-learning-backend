FROM python:3
WORKDIR /sufle/learning/app

COPY requirements.txt .
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
