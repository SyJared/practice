FROM python:3.12-slim AS builder
WORKDIR /app
COPY app/main.py .
COPY tests/ ./tests
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/main.py .
ENV APP_MODE=prod
CMD ["python3", "main.py"]
