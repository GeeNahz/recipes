FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app/backend

# install system dependencies
RUN apt update && \
    apt upgrade -y && \
    apt install -y libpq-dev python3-dev build-essential postgresql-server-dev-all

# install dependencies
RUN pip install --upgrade pip
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
