import requests
from .heuristics import analyze_heuristics

def get_tx_data(address, api_key=None):
    base_url = f"https://api.blockchair.com/bitcoin/dashboards/address/{address}"
    if api_key:
        base_url += f"?key={api_key}"

    response = requests.get(base_url)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    
    data = response.json()
    txs = data['data'][address]['transactions']
    return txs[:100]  # Ограничим для бесплатного анализа

def analyze_address(address, api_key=None):
    try:
        txs = get_tx_data(address, api_key)
        return analyze_heuristics(txs)
    except Exception as e:
        return f"Error during analysis: {e}"
