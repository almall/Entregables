FROM python:3.9.12
COPY ./Maggie.py /app/
COPY ./docker.txt /app/

WORKDIR /app/
RUN mkdir General
RUN mkdir Homer
RUN mkdir Lisa
RUN pip3 install -r ./docker.txt

CMD ["python","Maggie.py"] 


