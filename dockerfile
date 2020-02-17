FROM python:alpine3.7
COPY /src /app
WORKDIR /app
RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]