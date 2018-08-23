FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django
WORKDIR /django
COPY . /django
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "start_web.py"]
