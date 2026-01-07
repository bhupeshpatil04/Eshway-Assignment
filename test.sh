#!/bin/bash
set -e

case "$1" in
base)
  pytest
  ;;
new)
  pytest tests/test_response_json_empty.py
  ;;
*)
  echo "Usage: ./test.sh {base|new}"
  exit 1
  ;;
esac
