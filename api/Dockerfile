FROM python:2.7-alpine
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]