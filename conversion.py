import requests
from bs4 import BeautifulSoup

def obtener_tasa_cambio(moneda_origen, moneda_destino):
    """
    Obtiene la tasa de cambio entre dos monedas sin API key.
    Fuente: https://www.x-rates.com
    """
    url = f"https://www.x-rates.com/calculator/?from={moneda_origen}&to={moneda_destino}&amount=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code != 200:
        raise Exception("Error al obtener la tasa de cambio.")

    sopa = BeautifulSoup(respuesta.text, "lxml")
    tasa = sopa.find("span", class_="ccOutputTrail").previous_sibling
    return float(tasa.replace(",", ""))

def convertir_divisa(monto, moneda_origen, moneda_destino):
    """
    Convierte un monto de una divisa a otra usando tasas en tiempo real.
    """
    tasa = obtener_tasa_cambio(moneda_origen, moneda_destino)
    return monto * tasa

# Ejemplo de uso
if __name__ == "__main__":
    moneda_origen = "USD"
    moneda_destino = "EUR"
    monto = 100

    try:
        resultado = convertir_divisa(monto, moneda_origen, moneda_destino)
        print(f"{monto} {moneda_origen} equivale a {resultado:.2f} {moneda_destino}")
    except Exception as e:
        print(f"Error: {e}")
