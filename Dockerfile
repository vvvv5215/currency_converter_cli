FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir requests
COPY converter.py ./
ENTRYPOINT ["python", "converter.py"] 