FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN  python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto
EXPOSE 5001

CMD ["python", "server.py"]