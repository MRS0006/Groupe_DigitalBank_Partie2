from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
print("🚀 API DigitalBank - Chargement du modèle...")
try:
    model = joblib.load('fraud_model.pkl')
    print("✅ Modèle Random Forest chargé !")
except Exception as e:
    print(f"⚠️  Mode test : {e}")
    model = None

@app.route('/')
def home():
    return jsonify({
        "projet": "DigitalBank - Détection de fraude",
        "équipe": "Groupe DigitalBank",
        "status": "🟢 En ligne",
        "message": "API opérationnelle pour analyser les transactions",
        "endpoints": {
            "accueil": "GET /",
            "santé": "GET /health",
            "prédiction": "POST /predict"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Analyse une transaction bancaire"""
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "Envoyez des données JSON"}), 400
        
        # Mode test si pas de modèle
        if model is None:
            return jsonify({
                "prediction": 0,
                "probability": 0.25,
                "risk": "Faible",
                "message": "Mode test - Modèle non chargé",
                "montant": data.get('montant', 0)
            })
        
        # TES FEATURES ICI (modifie selon ton modèle)
        features = [
            data.get('montant', 0),
            data.get('heure', 12),
            data.get('age_client', 30),
            data.get('salaire_annuel', 50000),
            data.get('score_credit', 700)
        ]
        
        # Prédiction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]
        
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability),
            "risk_level": "Élevé" if probability > 0.7 else "Moyen" if probability > 0.3 else "Faible",
            "transaction_analyzed": True,
            "message": "Fraude détectée" if prediction == 1 else "Transaction normale"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# IMPORTANT pour Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🌍 Serveur démarré sur le port {port}")
    app.run(host='0.0.0.0', port=port)from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
print("🚀 API DigitalBank - Chargement du modèle...")
try:
    model = joblib.load('fraud_model.pkl')
    print("✅ Modèle Random Forest chargé !")
except Exception as e:
    print(f"⚠️  Mode test : {e}")
    model = None

@app.route('/')
def home():
    return jsonify({
        "projet": "DigitalBank - Détection de fraude",
        "équipe": "Groupe DigitalBank",
        "status": "🟢 En ligne",
        "message": "API opérationnelle pour analyser les transactions",
        "endpoints": {
            "accueil": "GET /",
            "santé": "GET /health",
            "prédiction": "POST /predict"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Analyse une transaction bancaire"""
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "Envoyez des données JSON"}), 400
        
        # Mode test si pas de modèle
        if model is None:
            return jsonify({
                "prediction": 0,
                "probability": 0.25,
                "risk": "Faible",
                "message": "Mode test - Modèle non chargé",
                "montant": data.get('montant', 0)
            })
        
        # TES FEATURES ICI (modifie selon ton modèle)
        features = [
            data.get('montant', 0),
            data.get('heure', 12),
            data.get('age_client', 30),
            data.get('salaire_annuel', 50000),
            data.get('score_credit', 700)
        ]
        
        # Prédiction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]
        
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability),
            "risk_level": "Élevé" if probability > 0.7 else "Moyen" if probability > 0.3 else "Faible",
            "transaction_analyzed": True,
            "message": "Fraude détectée" if prediction == 1 else "Transaction normale"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# IMPORTANT pour Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🌍 Serveur démarré sur le port {port}")
    app.run(host='0.0.0.0', port=port)from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
print("🚀 API DigitalBank - Chargement du modèle...")
try:
    model = joblib.load('fraud_model.pkl')
    print("✅ Modèle Random Forest chargé !")
except Exception as e:
    print(f"⚠️  Mode test : {e}")
    model = None

@app.route('/')
def home():
    return jsonify({
        "projet": "DigitalBank - Détection de fraude",
        "équipe": "Groupe DigitalBank",
        "status": "🟢 En ligne",
        "message": "API opérationnelle pour analyser les transactions",
        "endpoints": {
            "accueil": "GET /",
            "santé": "GET /health",
            "prédiction": "POST /predict"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Analyse une transaction bancaire"""
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "Envoyez des données JSON"}), 400
        
        # Mode test si pas de modèle
        if model is None:
            return jsonify({
                "prediction": 0,
                "probability": 0.25,
                "risk": "Faible",
                "message": "Mode test - Modèle non chargé",
                "montant": data.get('montant', 0)
            })
        
        # TES FEATURES ICI (modifie selon ton modèle)
        features = [
            data.get('montant', 0),
            data.get('heure', 12),
            data.get('age_client', 30),
            data.get('salaire_annuel', 50000),
            data.get('score_credit', 700)
        ]
        
        # Prédiction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]
        
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability),
            "risk_level": "Élevé" if probability > 0.7 else "Moyen" if probability > 0.3 else "Faible",
            "transaction_analyzed": True,
            "message": "Fraude détectée" if prediction == 1 else "Transaction normale"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# IMPORTANT pour Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🌍 Serveur démarré sur le port {port}")
    app.run(host='0.0.0.0', port=port)from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Charger le modèle
print("🚀 API DigitalBank - Chargement du modèle...")
try:
    model = joblib.load('fraud_model.pkl')
    print("✅ Modèle Random Forest chargé !")
except Exception as e:
    print(f"⚠️  Mode test : {e}")
    model = None

@app.route('/')
def home():
    return jsonify({
        "projet": "DigitalBank - Détection de fraude",
        "équipe": "Groupe DigitalBank",
        "status": "🟢 En ligne",
        "message": "API opérationnelle pour analyser les transactions",
        "endpoints": {
            "accueil": "GET /",
            "santé": "GET /health",
            "prédiction": "POST /predict"
        }
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Analyse une transaction bancaire"""
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "Envoyez des données JSON"}), 400
        
        # Mode test si pas de modèle
        if model is None:
            return jsonify({
                "prediction": 0,
                "probability": 0.25,
                "risk": "Faible",
                "message": "Mode test - Modèle non chargé",
                "montant": data.get('montant', 0)
            })
        
        # TES FEATURES ICI (modifie selon ton modèle)
        features = [
            data.get('montant', 0),
            data.get('heure', 12),
            data.get('age_client', 30),
            data.get('salaire_annuel', 50000),
            data.get('score_credit', 700)
        ]
        
        # Prédiction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]
        
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability),
            "risk_level": "Élevé" if probability > 0.7 else "Moyen" if probability > 0.3 else "Faible",
            "transaction_analyzed": True,
            "message": "Fraude détectée" if prediction == 1 else "Transaction normale"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# IMPORTANT pour Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"🌍 Serveur démarré sur le port {port}")
    app.run(host='0.0.0.0', port=port)
