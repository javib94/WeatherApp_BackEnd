FROM python:3.8
  
WORKDIR /usr/src/

RUN pip install pipenv

ENV DB_URL='database'

ENV DB_PORT='3306'

ENV DB_NAME='weatherdb'

ENV DB_USER='weatheruser'
    
ENV DB_PASSWORD='weatherpass'

COPY . .

RUN pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["./bootstrap.sh" ] 