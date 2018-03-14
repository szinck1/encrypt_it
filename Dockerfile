FROM python:3.6
LABEL Description="encrypt_it" Vendor="Canadian Digital Service"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

CMD ["gunicorn", "--pythonpath=src/encrypt_it", "--bind=0.0.0.0:5010", "encrypt_it.app:app"]
