#!/bin/bash

export APP_NAME=${APP_NAME:-app}
export HOST_IP=${HOST_IP:-0.0.0.0}
export HOST_PORT=${HOST_PORT:-5000}

CMD="$@"
if [ -z "$CMD" ]; then
  CMD="python ${APP_NAME}.py runserver --host=${HOST_IP} --port=${HOST_PORT} --threaded"
fi

echo "Starting server ..."
exec $CMD