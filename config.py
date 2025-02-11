from dotenv import load_dotenv
import os
import streamlit as st

# Chargement des variables d'environnement
load_dotenv()

# Configuration des APIs - Priorité aux secrets Streamlit si disponibles
MARKETSTACK_API_KEY = st.secrets["MARKETSTACK_API_KEY"] if "MARKETSTACK_API_KEY" in st.secrets else os.getenv('MARKETSTACK_API_KEY')
DEEPSEEK_API_KEY = st.secrets["DEEPSEEK_API_KEY"] if "DEEPSEEK_API_KEY" in st.secrets else os.getenv('DEEPSEEK_API_KEY')

# URLs de base
MARKETSTACK_BASE_URL = 'http://api.marketstack.com/v1'
DEEPSEEK_BASE_URL = 'https://api.deepseek.com'

# Configuration par défaut pour l'analyse
DEFAULT_TIMEFRAME = '1h'
MIN_PIPS_TARGET = 20
MAX_PIPS_TARGET = 30 