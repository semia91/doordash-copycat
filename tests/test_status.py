# tests/test_status.py
import httpx

def test_service_status():
    # On teste l'endpoint /status/ que tu as trouvé dans le main.py
    response = httpx.get("http://localhost:8090/status/")
    
    assert response.status_code == 200
    assert response.json() == {"status": "Service is up and running"}