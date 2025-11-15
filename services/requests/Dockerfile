FROM python:3.10.12-slim

COPY . /requests
WORKDIR /requests

RUN pip install -r requirements.txt

CMD ["python3", "req.py" ]

# docker build . --tag test_requests:2
# docker run test_requests:2