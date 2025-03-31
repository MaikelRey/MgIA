instalar dependencias:
pip install -r requirements.txt

arrancar fastapi y streamlit
uvicorn main:app --reload (deberia abrir o navegador en ://localhost:8000 o ://127.0.0:8000 que es lo mismo)

arrancar streamlit:
streamlit run main.py