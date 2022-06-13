FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN  python3 -m grpc_tools.protoc -I ./app --python_out=./app --grpc_python_out=./app location.proto
EXPOSE 5004
CMD ["python", "app/consumer.py"]