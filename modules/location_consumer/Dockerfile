FROM python:3.10-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN python3 -m grpc_tools.protoc -I./app/udaconnect --python_out=./app/udaconnect --grpc_python_out=./app/udaconnect app/udaconnect/location.proto


EXPOSE 5004

COPY . .
CMD ["python3", "app/udaconnect/consumer.py"]