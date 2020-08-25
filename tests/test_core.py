from hogwarts_apitest.number import __version__,__author__

def test_version():

    assert isinstance(__version__,str)

def test_author():
    assert isinstance(__author__,str)