FROM python:3.8
  
WORKDIR /usr/src/

RUN pip install pipenv

COPY . .

RUN pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["./bootstrap.sh" ] 