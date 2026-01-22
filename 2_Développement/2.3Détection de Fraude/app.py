# app.py - SIMPLIFIÉ AU MAXIMUM
from flask import Flask, request, jsonify
import joblib
import numpy as np

# 1. Créer l'application Flask
app = Flask(__name__)

# 2. Charger TON modèle (celui que tu as créé en Partie 1)
print("📦 Chargement du modèle...")
model = joblib.load('fraud_model.pkl')  # TON MODÈLE
print("✅ Modèle chargé !")

# 3. Définir la route principale
@app.route('/')
def home():
    return """
    <h1>API Détection Fraude - DigitalBank</h1>
    <p>Utilise POST /predict avec JSON</p>
    """

# 4. Définir la route de prédiction
@app.route('/predict', methods=['POST'])
def predict():
    """
    Exemple de données à envoyer :
    {
        "montant": 15000,
        "heure": 3,
        "jour_semaine": 6,
        "type_transaction": 2,
        "pays_destination": 5,
        "age_client": 25,
        "salaire_annuel": 30000,
        "score_credit": 550
    }
    """
    try:
        # A. Récupérer les données envoyées
        data = request.json
        
        # B. Préparer les données dans le bon ordre
        # IMPORTANT : Même ordre que lors de l'entraînement
        features = [
            data['montant'],
            data['heure'],
            data['jour_semaine'],
            data['type_transaction'],
            data['pays_destination'],
            data['age_client'],
            data['salaire_annuel'],
            data['score_credit']
        ]
        
        # C. Ajouter les features calculées (comme dans ton script)
        features.append(np.log1p(data['montant']))  # montant_log
        features.append(1 if data['montant'] > 10000 else 0)  # montant_suspect
        features.append(1 if (data['heure'] >= 22 or data['heure'] <= 5) else 0)  # est_nuit
        features.append(data['montant'] / ((data['salaire_annuel'] / 12) + 1))  # ratio
        
        # D. Faire la prédiction avec TON modèle
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]  # 0 ou 1
        probability = model.predict_proba(features_array)[0][1]  # % de fraude
        
        # E. Retourner la réponse
        return jsonify({
            'is_fraud': bool(prediction == 1),
            'fraud_score': float(probability),
            'fraud_percentage': round(probability * 100, 2),
            'message': 'HAUTE ALERTE' if probability > 0.8 else 'Surveillance' if probability > 0.5 else 'Normal'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 5. Lancer le serveur
if __name__ == '__main__':
    print("🚀 Lancement de l'API...")
    print("📍 Accès : http://localhost:5000")
    print("📍 Test : http://localhost:5000/predict")
    app.run(host='0.0.0.0', port=5000, debug=True)