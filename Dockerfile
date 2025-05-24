FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8080

# Create a startup script
RUN echo '#!/bin/bash\n\
exec uvicorn --host 0.0.0.0 --port $PORT main:app' > /app/start.sh \
    && chmod +x /app/start.sh

CMD ["/app/start.sh"]
