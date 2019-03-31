# We Use an official Python runtime as a parent image
# unified_pyweb_base image is built on top of an official Python image
FROM unified_pyweb_base:latest

COPY ./ ./app
WORKDIR ./app
RUN pipreqs --debug ./
RUN pip3 install -r ./requirements.txt

CMD ["gunicorn", "-w 4", "server:app"]
 
