import pytest
from requests.models import Response

def make_response(content):
    r = Response()
    r._content = content
    r.encoding = "utf-8"
    return r

def test_json_empty_string_raises_value_error():
    r = make_response(b"")
    with pytest.raises(ValueError, match="Response body is empty"):
        r.json()

def test_json_whitespace_raises_value_error():
    r = make_response(b"   \n\t  ")
    with pytest.raises(ValueError, match="Response body is empty"):
        r.json()

def test_json_invalid_non_empty_still_raises_json_error():
    r = make_response(b"{invalid json}")
    with pytest.raises(Exception):
        r.json()

def test_json_valid_still_works():
    r = make_response(b'{"key": "value"}')
    assert r.json() == {"key": "value"}
