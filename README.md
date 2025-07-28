# 📢 Publicador de Productos en Telegram

Esta app en Streamlit permite publicar productos aleatorios desde WooCommerce en un canal o grupo de Telegram.

## Configuración

Debes establecer las siguientes variables de entorno:

- WOOCMERCE_URL
- WOOCMERCE_CK
- WOOCMERCE_CS
- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID

Puedes hacer esto en Streamlit Cloud usando `.streamlit/secrets.toml`.

## Uso

1. Ejecuta la app con `streamlit run app.py`
2. Presiona el botón para publicar un producto aleatorio
3. Consulta el historial de publicaciones
