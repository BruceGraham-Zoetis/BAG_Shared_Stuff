import pytest
import my_analyzer


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(
        my_analyzer, 'PETS', [my_analyzer.Pet(id=1, name='a'), my_analyzer.Pet(id=2, name='b')]
    )
    with my_analyzer.app.test_client() as client:
        yield client


def test_collection_post(client):
    response = client.post('/api/v1/pets', json={'name': 'c'})
    assert response.json == {'id': 3, 'name': 'c'}


def test_collection_get(client):
    response = client.get('/api/v1/pets')
    assert response.json == [
        {'id': 1, 'name': 'a'},
        {'id': 2, 'name': 'b'},
    ]


def test_item_get(client):
    response = client.get('/api/v1/pets/1')
    assert response.json == {'id': 1, 'name': 'a'}

    response = client.get('/api/v1/pets/3')
    assert response.status_code == 404
