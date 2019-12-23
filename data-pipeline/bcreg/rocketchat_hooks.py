from os import environ
import asyncio
import aiohttp
import concurrent.futures

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

pool = concurrent.futures.ThreadPoolExecutor()

def synchronous_post_url(webhook_url, payload):
    return pool.submit(asyncio.run, _post_url(webhook_url, payload)).result(timeout=30)


def post_msg_to_webhook(level, message):
    if webhook_url and 0 < len(webhook_url):
        if level and level <= log_level:
            payload = get_webhook_payload(level, message)
            try:
                (status, text) = synchronous_post_url(webhook_url, payload)
                print(">>> Posted webhook level", level, "with message", message)
                print(">>> Returned", status, text)
            except Exception as e:
                print(">>> NOT posted webhook, error:", str(e))
        else:
            print(">>> NOT Posted webhook level", level, "(", log_level, "), message", message)
    else:
        print(">>> NOT Posted webhook level", level, "message", message, "no webhook_url")


def log_info(message):
    post_msg_to_webhook('2', message)


def log_warning(message):
    post_msg_to_webhook('1', message)


def log_error(message):
    post_msg_to_webhook('0', message)