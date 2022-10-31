FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8000
WORKDIR /secoda 
COPY requirements.txt /secoda
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /secoda 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]