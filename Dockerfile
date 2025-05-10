FROM python:3.12-slim-bookworm

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8181
CMD ["python", "app.py"]