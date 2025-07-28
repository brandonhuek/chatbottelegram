import streamlit as st
from woocommerce_api import get_random_product
from telegram_bot import send_product_to_telegram, log_publication
import pandas as pd
import os

st.set_page_config(page_title="Publicador Telegram", layout="wide")
st.title("📢 Publicador de Productos en Telegram")

if st.button("📤 Publicar producto aleatorio ahora"):
    product = get_random_product()
    if product:
        send_product_to_telegram(product)
        log_publication(product, "Manual")
        st.success(f"Publicado: {product['name']}")
    else:
        st.warning("No se pudo obtener un producto.")

st.subheader("📚 Historial de publicaciones")
if os.path.exists("historial.csv"):
    df = pd.read_csv("historial.csv")
    st.dataframe(df)
else:
    st.write("Aún no hay publicaciones registradas.")
