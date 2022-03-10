FROM python:3.7
LABEL maintainer Serzh Ok <okruz2612@gmail.com>

COPY . /app
WORKDIR /app

RUN python3 --version
RUN pip3 --version
RUN pip install -r requirements.txt

EXPOSE 8180
EXPOSE 8181

CMD ["python3", "/app/predict.py"]