FROM python:3.11.3-slim

RUN python3 -m venv /opt/venv

CMD ["mkdir", "app/web"]

WORKDIR /app/web
COPY ./apps/web/ .

RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r /app/web/requirements.txt && \
    chmod +x /app/web/scripts/entrypoint.sh

CMD ["/app/web/scripts/entrypoint.sh"]


