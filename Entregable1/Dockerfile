FROM python 3.11.0
COPY ./Lisa.py /app/
COPY ./requirements.txt /app/
WORKDIR /app/
RUN pip3 install -r ./requirements.txt

CMD ["python" , "Lisa.py"] 
