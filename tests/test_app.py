from fastapi import status
from fastapi.testclient import TestClient

from fast_zero.app import app  # Importa o app do seu arquivo existente


def test_read_root_deve_retornar_200_e_mensagem_correta():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World, from FastAPI"}
