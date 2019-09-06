#!/bin/bash

export APP_NAME=${APP_NAME:-app}
export HOST_IP=${HOST_IP:-0.0.0.0}
export HOST_PORT=${HOST_PORT:-5000}

CMD="$@"
if [ -z "$CMD" ]; then
  CMD="flask run --host=${HOST_IP} --port=${HOST_PORT} --with-threads --reload --eager-loading"
fi

echo "Starting server ..."
exec $CMD
