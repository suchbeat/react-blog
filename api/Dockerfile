FROM python:2.7-alpine
COPY requirements.txt /api/requirements.txt
RUN pip install -r /api/requirements.txt
COPY . /api
WORKDIR /api
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]