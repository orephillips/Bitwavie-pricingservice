FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt gunicorn

ENV PORT=8080

# Create a startup script
RUN echo '#!/bin/bash\n\
exec gunicorn --bind :$PORT --workers 1 main:get_price' > /app/start.sh \
    && chmod +x /app/start.sh

CMD ["/app/start.sh"]
