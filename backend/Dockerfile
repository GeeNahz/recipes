FROM python:3.10-alpine3.19

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app/backend

# install system dependencies
RUN apk --no-cache update && \
    apk --no-cache add alpine-sdk && \
    apk --no-cache add python3 python3-dev python3-tests libssl3 openldap-dev openssl-dev net-snmp-dev py3-setuptools py3-wheel sqlite postgresql postgresql-client postgresql-dev gcc musl-dev


# install dependencies
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint.sh script into the container and make it executable
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/backend/entrypoint.sh
RUN chmod +x /usr/src/app/backend/entrypoint.sh

# Copy the wait-for-postgres.sh script into the container and make it executable
COPY ./waitforpostgres.sh .
RUN sed -i 's/\r$//g' /usr/src/app/backend/waitforpostgres.sh
RUN chmod +x /usr/src/app/backend/waitforpostgres.sh

COPY . .

EXPOSE 8000

# Set the container's entrypoint to the entrypoint.sh script
ENTRYPOINT ["/usr/src/app/backend/entrypoint.sh"]
