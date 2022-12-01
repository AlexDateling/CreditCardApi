FROM python:3.9-alpine


WORKDIR /usr/app
COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "./src/creditCardApi.py"]