
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_somar():
    resposta = client.get("/somar/10/20")
    assert resposta.status_code == 200
    assert resposta.json() == {"resultado": 30}
 