FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

WORKDIR /usr/src/app/src
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]