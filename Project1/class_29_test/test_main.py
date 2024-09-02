from fastapi.testclient import TestClient

from testing_and_debugging import app

client = TestClient(app)

def test_read_items():
    response = client.get("/items/foo",headers={'X-Token' : 'coneofsilence'})
    assert response.status_code == 200
    assert response.json() =={
        'id':'foo',
        'title' : 'Foo',
        'description' : "There goes my hero"
    }


def test_read_item_bad_token():
    response = client.get("/items/foo",headers={'X-Token' : 'wrong'})
    assert response.status_code == 400
    assert response.json() == {'detail' : "Invalid X-Token header"}

def test_read_inexistent_item():
    response = client.get("/items/baz",headers={'X-Token' : 'coneofsilence'})
    assert response.status_code == 404
    assert response.json() == {'detail' : "Item not found"}

def test_create_item():
    response = client.post("/items/",
                           json={'id': 'foobar', 'title': "Foo Bar",'description' :"the Foo Bartenders"},
                            headers={'X-Token' : 'coneofsilence'})
    assert response.status_code == 200
    assert response.json() == {'id': 'foobar', 'title': "Foo Bar",'description' :"the Foo Bartenders"}


def test_create_item_bad_token():
    response = client.post("/items/",
                           json={'id': 'bz', 'title': "Baz",'description' :"Drop the Baz"},
                            headers={'X-Token' : 'wrong'})
    assert response.status_code == 400
    assert response.json() == {'detail' : "Invalid X-Token header"}

def test_create_existing_item():
    response = client.post("/items/",
                           json={'id': 'foo', 'title': "Foo",'description' :"There goes my hero"},
                            headers={'X-Token' : 'coneofsilence'})
    assert response.status_code == 400
    assert response.json() == {'detail':"Item already exists"}
