FROM python:3.10-alpine
ARG LOG_PATH
RUN apk add --no-cache tshark coreutils
WORKDIR /code
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "tshark_runner.py", "hostnames.json", "${LOG_PATH}"]