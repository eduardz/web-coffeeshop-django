FROM python:3.11.1-slim

# App setup
COPY ./coffeeshop /coffeeshop
WORKDIR /coffeeshop

# Requirements installation
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
