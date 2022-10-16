# pull official base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /app



# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./venv_requirements.txt /app/venv_requirements.txt
RUN pip install -r venv_requirements.txt

ENV FLASK_APP /app/app/app.py
# copy project
COPY . .


CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "app.app:create_app()"]
# CMD ["flask", "run"]