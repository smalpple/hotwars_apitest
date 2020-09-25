from hogwarts_apitest.number import __version__,__author__
import requests

def test_version():
    assert isinstance(__version__,str)

def test_author():
    assert isinstance(__author__,str)

def test_httpbin_get():
    res = requests.get("https://httpbin.org/get",
                       headers={"accept":"application/json"})

    assert res.status_code == 200
    assert res.headers["server"] == "gunicorn/19.9.0"
