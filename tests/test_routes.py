from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_shorten_url():
    data = {'url': 'https://www.google.com'}
    response = client.post('/', json=data)

    assert response.status_code == 201
    assert 'shorten_id' in response.json()


def test_shorten_url_empty():
    data = {'url': ''}
    response = client.post('/', json=data)

    assert response.status_code == 400
    assert response.json() == {'detail': 'Empty URL'}


def test_get_morty():
    response = client.get('/morty')

    assert response.status_code == 200
    data = response.json()
    assert 'name' in data
    assert 'status' in data
    assert 'image' in data


def test_redirect_url():
    data = {'url': 'https://www.google.com'}
    response = client.post('/', json=data)
    shorten_id = response.json()['shorten_id']

    response = client.get(f'/{shorten_id}', follow_redirects=False)

    assert response.status_code == 307
    assert response.headers['Location'] == 'https://www.google.com'
