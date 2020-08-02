#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${DIR}/serial_logger/bin/activate
python2 -u ${DIR}/logger.py "$@"
