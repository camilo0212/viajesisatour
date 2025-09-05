# configuración_de_firebase.py

import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json

def init_firebase():
    """
    Inicializa la conexión con Firebase de forma robusta,
    asegurando que las credenciales se pasen como un diccionario.
    """
    # Evita reinicializar la app en cada recarga de la página
    if not firebase_admin._apps:
        # Extrae las credenciales desde los secretos de Streamlit
        firebase_secrets = st.secrets["firebase"]

        # Construimos un diccionario Python a partir de los secretos.
        # Esto asegura que el formato es un diccionario y no un string.
        creds_dict = {
            "type": firebase_secrets["type"],
            "project_id": firebase_secrets["project_id"],
            "private_key_id": firebase_secrets["private_key_id"],
            # Esta línea es CRUCIAL: formatea correctamente la clave privada
            "private_key": firebase_secrets["private_key"].replace('\\n', '\n'),
            "client_email": firebase_secrets["client_email"],
            "client_id": firebase_secrets["client_id"],
            "auth_uri": firebase_secrets["auth_uri"],
            "token_uri": firebase_secrets["token_uri"],
            "auth_provider_x509_cert_url": firebase_secrets["auth_provider_x509_cert_url"],
            "client_x509_cert_url": firebase_secrets["client_x509_cert_url"]
        }

        # Inicializa la app de Firebase con el diccionario de credenciales
        creds = credentials.Certificate(creds_dict)
        firebase_admin.initialize_app(creds)

    # Devuelve el cliente de Firestore para poder usar la base de datos
    return firestore.client()
