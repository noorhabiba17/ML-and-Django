import joblib
import numpy as np
from django.shortcuts import render, redirect
from .models import ParticlePrediction

# Load model and scaler once at startup
try:
    model = joblib.load('svm_model.pkl')
    scaler = joblib.load('scaler.pkl')
except:
    model = None
    scaler = None

def predict_particle(request):
    result = None
    # Fetch history for the modal
    history = ParticlePrediction.objects.all().order_by('-created_at')

    if request.method == 'POST':
        bulk_input = request.POST.get('bulk_array')
        if bulk_input:
            try:
                # 1. Process Input
                input_values = [float(x.strip()) for x in bulk_input.split(',')]
                if len(input_values) != 10:
                    raise ValueError("Exactly 10 values required.")

                # 2. ML Prediction
                data_reshaped = np.array(input_values).reshape(1, -1)
                data_scaled = scaler.transform(data_reshaped)
                prediction_numeric = model.predict(data_scaled)[0]
                result = "Gamma" if prediction_numeric == 1 else "Hadron"

                # 3. Save to SQLite
                ParticlePrediction.objects.create(
                    fLength=input_values[0], fWidth=input_values[1], fSize=input_values[2],
                    fConc=input_values[3], fConc1=input_values[4], fAsym=input_values[5],
                    fM3Long=input_values[6], fM3Trans=input_values[7], fAlpha=input_values[8],
                    fDist=input_values[9], prediction_label=result
                )
                # Refresh history after save
                history = ParticlePrediction.objects.all().order_by('-created_at')

            except Exception as e:
                result = f"Error: {str(e)}"

    return render(request, 'Home/predict.html', {'result': result, 'history': history})

def delete_history(request):
    if request.method == 'POST':
        ParticlePrediction.objects.all().delete()
    return redirect('predict')


import csv
from django.http import HttpResponse

import csv
from django.http import HttpResponse

# Ensure this name matches exactly what is in your urls.py
def export_history_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="particle_history.csv"'

    writer = csv.writer(response)
    # Header row
    writer.writerow(['Timestamp', 'Result', 'fLength', 'fWidth', 'fSize', 'fAlpha'])

    # Get data from database
    history = ParticlePrediction.objects.all().order_by('-created_at')
    
    for p in history:
        writer.writerow([
            p.created_at.strftime("%Y-%m-%d %H:%M:%S"), 
            p.prediction_label, 
            p.fLength, 
            p.fWidth, 
            p.fSize, 
            p.fAlpha
        ])

    return response