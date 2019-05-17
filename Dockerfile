FROM python:3.6.1
EXPOSE 5254
WORKDIR /
RUN mkdir /app && chmod 755 /app
RUN apt-get update && apt-get install -y \
    vim
RUN pip install flask \
 flask_restplus \
 requests \
 pycurl \
 pyopenssl

RUN pip install -U flask-cors
COPY . /app
WORKDIR /app/
ENV LOG_LEVEL="DEBUG"
#ENV PATH="/usr/local/bin:${PATH}"
COPY . /app
WORKDIR /app/
RUN chmod 755 app.py
CMD python app.py -p 5254 
