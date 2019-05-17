FROM python:3.6.1
EXPOSE 5254
WORKDIR /
RUN mkdir /app && chmod 755 /app
#RUN apt-get update
RUN pip install flask \
 flask_restplus \
 requests \
 pycurl \
 pyopenssl

RUN pip install -U flask-cors
COPY . /app
WORKDIR /app/
ENV LOG_LEVEL="DEBUG"
COPY . /app
WORKDIR /app/
RUN chmod 755 app.py
CMD python app.py
