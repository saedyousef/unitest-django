FROM python:3.7
WORKDIR /Users/saedyousef/web/src/app
ADD requirements.txt /Users/saedyousef/web/src/app
RUN pip install -r requirements.txt
ADD . /Users/saedyousef/web/src/app
