# tests/test_root.py
import httpx

def test_read_root():
    # On envoie une requête GET sur l'API qui tourne dans Docker
    response = httpx.get("http://localhost:8090/")
    
    # On vérifie le code HTTP (200 = OK) et le message
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the DoorDash Delivery Fee Service API"}