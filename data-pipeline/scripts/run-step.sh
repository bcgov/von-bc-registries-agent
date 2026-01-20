#!/bin/bash
export RUN_LEAR_PIPELINE_STEPS_INDIVIDUALLY=${RUN_LEAR_PIPELINE_STEPS_INDIVIDUALLY:-true}

function runLearPipelineSteps() {
    echo "Running the LEAR pipeline steps individually ..." >&2
    # Find unprocessed events ...
    PYTHONPATH=. python3 "bcreg/find-unprocessed-events-lear.py"

    # Find process the events ...
    PYTHONPATH=. python3 "bcreg/process-corps-generate-creds_lear.py"
    PYTHONPATH=. python3 "bcreg/generate-creds_lear.py"
    PYTHONPATH=. python3 "bcreg/submit-creds_lear.py"
}

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

    if [[ "$@" == "bcreg/bc_reg_pipeline_lear.py" && "${RUN_LEAR_PIPELINE_STEPS_INDIVIDUALLY}" == true ]]; then
        runLearPipelineSteps
    else
        # Run the requested pipeline
        PYTHONPATH=. python3 "$@"
    fi
) 200>|"${lockFileName}"

popd >/dev/null
