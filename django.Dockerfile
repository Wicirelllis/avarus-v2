FROM python:3.12.3-bookworm

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR avarus
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
