FROM python:3.6

ENV http_proxy http://10.213.96.52:3128/
ENV https_proxy http://10.213.96.52:3128/

COPY ./ ./app
WORKDIR ./app

RUN pip3 install pipreqs
RUN pipreqs  --debug ./
RUN dir ./
RUN cat ./base-requirements.txt >> requirements.txt 
RUN cat ./requirements.txt  
RUN pip3 install -r ./requirements.txt
CMD ["gunicorn", "-w 4", "server:app"]
 
