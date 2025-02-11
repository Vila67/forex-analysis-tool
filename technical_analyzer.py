from openai import OpenAI
import requests
import pandas as pd
from datetime import datetime
import config

class TechnicalAnalyzer:
    def __init__(self):
        self.marketstack_client = requests.Session()
        import openai
        openai.api_key = config.DEEPSEEK_API_KEY
        openai.api_base = config.DEEPSEEK_BASE_URL
        self.deepseek_client = openai
        
    def get_market_data(self, symbol, timeframe=config.DEFAULT_TIMEFRAME):
        """Récupère les données du marché via MarketStack"""
        endpoint = f"{config.MARKETSTACK_BASE_URL}/intraday"
        params = {
            'access_key': config.MARKETSTACK_API_KEY,
            'symbols': symbol,
            'interval': timeframe
        }
        
        response = self.marketstack_client.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        return None
        
    def analyze_market_conditions(self, market_data):
        """Analyse les conditions du marché via DeepSeek"""
        prompt = self._create_analysis_prompt(market_data)
        
        response = self.deepseek_client.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Vous êtes un analyste technique expert."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
        
    def _create_analysis_prompt(self, market_data):
        """Crée un prompt détaillé pour l'analyse"""
        return f"""
        Analysez les conditions de marché suivantes :
        Prix actuel: {market_data['data'][0]['close']}
        Volume: {market_data['data'][0]['volume']}
        
        Identifiez les opportunités de trading avec :
        - Un objectif minimum de {config.MIN_PIPS_TARGET} pips
        - Un objectif maximum de {config.MAX_PIPS_TARGET} pips
        
        Fournissez une analyse détaillée incluant :
        1. La tendance principale
        2. Les niveaux de support/résistance
        3. Les signaux d'entrée potentiels
        4. Les objectifs de prix
        5. Les niveaux de stop-loss recommandés
        """ 