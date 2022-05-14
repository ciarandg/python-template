FROM python:3.9

WORKDIR /usr/src/app

RUN pip install poetry

COPY . .

CMD [ "./build_run.sh" ]
