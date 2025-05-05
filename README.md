# 🔥 CORS Checker

Herramienta simple en Python para detectar vulnerabilidades de configuración CORS en APIs autenticadas.

## 🧠 Características

- Evalúa encabezados `Access-Control-Allow-Origin` y `Access-Control-Allow-Credentials`
- Soporte para token Bearer
- Salida en colores
- Banner estilo hacker 🐱‍💻

## 🚀 Uso

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 check_cors.py -u https://api.ejemplo.com/data -t TU_TOKEN
```

## ⚠️ Advertencia
**Usar únicamente con fines éticos y en entornos autorizados.**
