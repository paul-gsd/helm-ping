FROM python:3.12.5-slim-bullseye

WORKDIR /app

COPY src/main.py .

EXPOSE 8080

CMD ["python", "main.py"]
