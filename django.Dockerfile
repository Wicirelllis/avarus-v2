FROM python:3.12.3-bookworm

RUN apt update && apt install -y gettext

ADD requirements.txt .

RUN pip install -r requirements.txt

WORKDIR avarus
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
