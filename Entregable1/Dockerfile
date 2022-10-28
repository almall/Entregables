FROM python 3.10.7
COPY ./Lisa.py /app/
COPY ./requirements.txt /app/
WORKDIR /app/
RUN pip3 install -r ./requirements.txt

CMD [ "python" , "Lisa.py"] 
