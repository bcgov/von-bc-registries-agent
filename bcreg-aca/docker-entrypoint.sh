#!/bin/bash

export APP_NAME=${APP_NAME:-app}
export APP_MODULE=${APP_MODULE:-${APP_NAME}:${APP_NAME}}
export HOST_IP=${HOST_IP:-0.0.0.0}
export HOST_PORT=${HOST_PORT:-5000}

CMD="$@"
if [ -z "$CMD" ]; then
  CMD="gunicorn --bind ${HOST_IP}:${HOST_PORT} ${APP_MODULE}"
fi

echo "Starting server ..."
exec $CMD