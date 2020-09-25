from hogwarts_apitest.number import __version__,__author__
import requests
import json

class ApiHttpBinGet:
    url = "https://httpbin.org/get"
    method = "GET"
    headers = {"accept":"application/json"}

    def run(self,params=None):
        res = requests.get(url=self.url,
                       headers=self.headers,
                       params=params)
        self.res = res
        return self

    def validate(self,key,expected_value):
        if "." in key:
            key_first,key_last = key.split(".")[0],key.split(".")[-1]
            actual_value = json.loads(
                json.dumps(
                dict(
                getattr(self.res,key_first))
                )
            )[key_last]
        else:
            actual_value = getattr(self.res,key)
            print(actual_value)
        assert actual_value == expected_value
        return self


def test_version():
    assert isinstance(__version__,str)

def test_author():
    assert isinstance(__author__,str)

def test_httpbin_get():
    ApiHttpBinGet().run(params={"abc":123})\
        .validate('status_code',200)\
        .validate('headers.Server',"gunicorn/19.9.0")\
        # .validate("json","https://httpbin.org/get?abc=123")


