FROM python:3
MKDIR code
WORKDIR code
RUN pip install -r requirements.txt
COPY . /code
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
