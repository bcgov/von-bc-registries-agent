from os import environ
import asyncio
import aiohttp

import time
import datetime

import json


LOG_LEVELS = {
    '0': 'ERROR',
    '1': 'WARNING',
    '2': 'INFO'
}

log_level = environ.get('WEBHOOK_LEVEL', '0')
if log_level > '2':
    log_level = '2'
elif log_level < '0':
    log_level = '0'

webhook_url = environ.get('WEBHOOK_URL', '')


def get_webhook_payload(level, message):
    project_name = environ.get('PROJECT_NAME', "von-bc-registries-agent")
    friendly_project_name = environ.get('FRIENDLY_PROJECT_NAME', "BC Registries")
    payload = {
        "friendlyProjectName": friendly_project_name,
        "projectName": project_name,
        "statusCode": LOG_LEVELS[level],
        "message": message
    }
    #payload = json.dumps(payload)
    return payload


async def _post_url(the_url, payload):
    async with aiohttp.ClientSession() as session:
        headers = {'Content-Type': 'application/json'}
        async with session.post(the_url, json=payload, headers=headers) as resp:
            r_status = resp.status
            r_text = await resp.text()
            return (r_status, r_text)


def run_coroutine_with_args(coroutine, *args):
    new_event_loop = True
    loop = asyncio.get_event_loop()
    if loop.is_running:
        new_event_loop = False
    try:
        if new_event_loop:
            return loop.run_until_complete(coroutine(*args))
        else:
            loop.create_task(coroutine(*args))
            return ('0', 'Message queued.')
    finally:
        if new_event_loop:
            loop.close()


def post_msg_to_webhook(level, message):
    if webhook_url and 0 < len(webhook_url):
        if level and level <= log_level:
            payload = get_webhook_payload(level, message)
            (status, text) = run_coroutine_with_args(_post_url, webhook_url, payload)


def log_info(message):
    post_msg_to_webhook('2', message)


def log_warning(message):
    post_msg_to_webhook('1', message)


def log_error(message):
    post_msg_to_webhook('0', message)