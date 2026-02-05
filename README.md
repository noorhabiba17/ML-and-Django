# ML-and-Django
# Radiation Classification System using Support Vector Machine (SVM)
![WhatsApp Image 2026-02-05 at 3 36 03 PM](https://github.com/user-attachments/assets/f9510d55-ac90-4079-ae40-60000288fb62)

![WhatsApp Image 2026-02-05 at 3 40 36 PM](https://github.com/user-attachments/assets/fb403c27-b058-4e73-ae03-2153c3d20d6a)


![WhatsApp Image 2026-02-05 at 3 36 02 PM](https://github.com/user-attachments/assets/1f600f2f-2f8c-45af-a591-0ebd61e84069)



This Django-based web application classifies atmospheric radiation into **Gamma (Signal)** or **Hadron (Background)**. It utilizes a **Support Vector Machine (SVM)** model to find the optimal hyperplane that separates the two particle classes based on Cherenkov telescope data.

## 🧠 Machine Learning: Support Vector Machine
The core of this project is an SVM classifier. SVM was chosen for its effectiveness in high-dimensional spaces and its ability to create a clear margin of separation between the complex features of Gamma and Hadron showers.



### Model Integration
The model is integrated directly into the Django backend:
- **Persistence:** The trained SVM model is loaded via `joblib` or `pickle` inside `views.py`.
- **Inference:** User inputs from the frontend are processed as a feature vector and passed to `model.predict()`.
- **Persistence:** Results are stored in the database linked to the SVM prediction output.

## 🚀 Features
- **SVM Prediction Engine:** High-accuracy classification using a radial basis function (RBF) or linear kernel.
- **Django Integration:** A seamless bridge between the Python ML logic and the web interface.
- **Database Tracking:** Every prediction is logged with its input parameters for further data analysis.

## 🛠️ Technical Implementation
### Views.py Logic
In your `views.py`, the flow operates as follows:
1. Capture `POST` data from the input form.
2. Scale the data (if a scaler was used during training).
3. Run the SVM model: `prediction = svm_model.predict(input_features)`.
4. Save the instance to the database: `ClassificationResult.objects.create(...)`.
5. Return the result to the template.

## 📂 Project Structure

<img width="398" height="686" alt="Screenshot 2026-02-05 152211" src="https://github.com/user-attachments/assets/b3769d07-7bc7-4995-84d1-03b14225b86e" />

# Any one who want to contribute they can add their valuable code
