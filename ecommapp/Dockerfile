FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY ./ /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]