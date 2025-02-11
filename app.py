import streamlit as st
from technical_analyzer import TechnicalAnalyzer
import time

def main():
    st.title("Analyse Technique en Temps Réel")
    
    # Initialisation de l'analyseur
    analyzer = TechnicalAnalyzer()
    
    # Sélection du symbole
    symbol = st.selectbox(
        "Sélectionnez une paire de devises",
        ["EURUSD", "GBPUSD", "USDJPY"]
    )
    
    # Sélection du timeframe
    timeframe = st.selectbox(
        "Sélectionnez un timeframe",
        ["15min", "30min", "1h", "4h"]
    )
    
    if st.button("Analyser"):
        with st.spinner("Analyse en cours..."):
            # Récupération des données
            market_data = analyzer.get_market_data(symbol, timeframe)
            
            if market_data:
                # Analyse des conditions
                analysis = analyzer.analyze_market_conditions(market_data)
                
                # Affichage des résultats
                st.subheader("Résultats de l'analyse")
                st.write(analysis)
            else:
                st.error("Erreur lors de la récupération des données")

if __name__ == "__main__":
    main() 