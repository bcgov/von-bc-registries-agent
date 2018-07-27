#
# Copyright 2017-2018 Government of Canada - Public Services and Procurement Canada - buyandsell.gc.ca
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

export HOST_IP=${HOST_IP:-127.0.0.1}
export HOST_PORT=${HOST_PORT:-5000}

# Generate passwd file based on current uid
function generate_passwd_file() {
  USER_ID=$(id -u)
  GROUP_ID=$(id -g)

  if [ x"$USER_ID" != x"0" -a x"$USER_ID" != x"1001" ]; then

    echo "default:x:${USER_ID}:${GROUP_ID}:Default Application User:${HOME}:/usr/sbin/nologin" >> /etc/passwd

  fi
}

CMD="$@"
if [ -z "$CMD" ]; then
  generate_passwd_file
  make
  source .venv/bin/activate
  CMD="flask run --host=${HOST_IP} --port=${HOST_PORT} --with-threads --reload --eager-loading"
fi

echo "Starting server ..."
exec $CMD