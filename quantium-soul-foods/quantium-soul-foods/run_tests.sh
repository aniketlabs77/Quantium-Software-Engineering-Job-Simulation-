#!/bin/bash

source venv/bin/activate

pytest tests/

if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
