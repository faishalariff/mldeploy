import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("FuelConsumption.csv")

# mengambil kolom yang dibutuhkan
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

# Training Data
# Gunakan semua data untuk pelatihan (train-test-split tidak digunakan)
x = cdf.iloc[:, :3]
y = cdf.iloc[:, -1]

regressor = LinearRegression()

# Memasukan data training ke dalam model
regressor.fit(x, y)

# menyimpan model menjadi .pkl
# Pickle membuat serial objek sehingga dapat disimpan ke file, dan dimuat dalam program lagi nanti.
pickle.dump(regressor, open('model.pkl','wb'))