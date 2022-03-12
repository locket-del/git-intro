import hello
import pytest

def test_string():
  assert type(hello.msg('HELLO')) == str
