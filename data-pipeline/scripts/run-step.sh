#!/bin/bash
pushd .. >/dev/null

# Use flock to get a non-blocking lock on a lockfile while a given pipeline is running
# to avoid multiple instances of the same pipeline from running.
# The lock files are purposely NOT deleted to avoid possible race conditions.
lockFileName=./$(basename "${@%%.*}").lock
(
    if ! flock -n 200; then
        echo "Another instance of ${@} is already running. Exiting." >&2
        exit 1
    fi

    # Run the requested pipeline
    PYTHONPATH=. python3 "$@"
) 200>|"${lockFileName}"

popd >/dev/null
