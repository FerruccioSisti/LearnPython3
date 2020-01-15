from nose.tools import *
from app import app

app.config["TESTING"] = True
web = app.test_client()

def test_index():
    rv = web.get("/", follow_redirects = True)
    assert_equal(rv.status_code, 404)

    rv = web.get("/hello", follow_redirects = True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    data = {"name": "Ferruccio", "greet": "hola"}
    rv = web.post("/hello", follow_redirects = True, data = data)
    assert_in(b"Ferruccio", rv.data)
    assert_in(b"hola", rv.data)
