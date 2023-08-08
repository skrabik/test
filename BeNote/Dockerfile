FROM python:3

COPY . .

RUN pip install django
RUN pip install psycopg2

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

