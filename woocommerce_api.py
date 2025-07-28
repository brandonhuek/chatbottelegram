import requests
import random
import os

def get_products():
    url = os.environ.get("WOOCOMMERCE_URL")
    ck = os.environ.get("WOOCOMMERCE_CK")
    cs = os.environ.get("WOOCOMMERCE_CS")

    # Verificar si la URL es válida
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("La URL de WooCommerce no está configurada correctamente. Asegúrate de incluir 'http://' o 'https://'.")

    response = requests.get(f"{url}/wp-json/wc/v3/products", auth=(ck, cs))
    if response.status_code == 200:
        return response.json()
    return []
