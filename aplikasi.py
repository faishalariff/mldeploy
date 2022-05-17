from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Menginisialisasi Flask
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

class App(object): 

    # page default aplikasi web
    @app.route('/')
    def home():
        return render_template('index.html')

    # Untuk menggunakan tombol prediksi di aplikasi web
    @app.route('/',methods=['POST'])
    def predict():

        # Untuk merender hasil pada GUI HTML
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text='CO2 Emission of the vehicle is :{}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)