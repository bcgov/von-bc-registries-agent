#!/usr/bin/env python3
#
# Copyright 2017-2018 Government of Canada
# Public Services and Procurement Canada - buyandsell.gc.ca
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import asyncio
import io
import os
import logging

from bcreg.bcreg_lear import lear_system_type
from bcreg.credssubmitter import CredsSubmitter
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


try:
    loop = asyncio.get_event_loop()
    with CredsSubmitter() as creds_submitter:
        loop.run_until_complete(creds_submitter.process_credential_queue(False, lear_system_type))
except Exception as e:
    print("Exception", e)
    log_error("submit_creds processing exception: " + str(e))
    raise

