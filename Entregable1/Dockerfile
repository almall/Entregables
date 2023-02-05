FROM python:3.9.12

WORKDIR /app/
COPY ./Lisa.py /app/
COPY ./docker.txt /app/

RUN pip3 install -r ./docker.txt

CMD ["python","Lisa.py"] 
