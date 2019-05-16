FROM python:3.6.1
EXPOSE 5254
WORKDIR /
RUN mkdir /infra && chmod 755 /infra
RUN apt-get update && apt-get install -y \
    vim
RUN pip install flask \ 
 flask_restplus \
 requests \
 pycurl \
 pyopenssl

RUN pip install -U flask-cors
COPY . /infra
WORKDIR /infra/
ENV LOG_LEVEL="DEBUG"
ENV PATH="/usr/local/bin:${PATH}" 
COPY . /infra
WORKDIR /infra/
RUN chmod 755 app.py
CMD python app.py -p 5254 
