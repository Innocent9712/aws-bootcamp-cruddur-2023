# FROM python:3.10-slim-buster

# WORKDIR /backend-flask

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# ENV FLASK_ENV=development

# EXPOSE ${PORT}
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]


# Stage 1 - Build
FROM python:3.10-slim-buster AS build
WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser /backend-flask \
    && pip3 install --user --no-cache-dir -r requirements.txt


USER appuser
COPY . .

# Stage 2 - Development
FROM python:3.10-slim-buster AS production
ENV PATH=/home/appuser/.local/bin:$PATH
ENV FLASK_ENV=development
WORKDIR /backend-flask

RUN apt-get update && apt-get install -y wget netcat



COPY --from=build /root/.local /usr/local


COPY . .


EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
