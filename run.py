import subprocess
import sys

def main():
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except Exception as e:
        print(f"Erreur lors du lancement : {e}")
        input("Appuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main() 