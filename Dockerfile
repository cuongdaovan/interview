FROM python:3.7

WORKDIR /Cinema

COPY . /Cinema
COPY Pipfile Pipfile.lock ./

RUN pip install -U pipenv
RUN pipenv install --system

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]