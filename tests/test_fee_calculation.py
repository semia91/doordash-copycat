# tests/test_fee_calculation.py
import httpx

def test_calculate_fee_valid():
    # On prépare les données à envoyer
    payload = {
        "distance_km": 2.0,
        "weight_kg": 4.0
    }
    
    # On fait une requête POST en envoyant le dictionnaire JSON
    response = httpx.post("http://localhost:8090/calculate-fee/", json=payload)
    
    # On vérifie que le calcul donne bien 10.0
    assert response.status_code == 200
    assert response.json() == {"delivery_fee": 10.0}