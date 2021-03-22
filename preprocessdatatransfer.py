# -*- coding: utf-8 -*-
"""PreprocessDataTransfer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lm25VuHeqSumPFri1l3Nfp8FXtJLkBni
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""import Library yang diperlukan"""

dataset = pd.read_csv('DataTransferPlayer.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""untuk mengambil semua baris
Untuk mengambil dan membaca dataset
"""

print(x)

print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

"""library machine learning untuk mengisi data kosong dengan mean/modus/mean.(SimpleImputer)
: , 1:3 = ambil semua baris, ambil komlom 1 sampai 3
"""

print(x)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

"""untuk data polinominal yang jenisnya lebih dari 2 harus diencoding dulu, dan akan dibuat menjadi matriks"""

print(x)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

"""input x, label y"""

print(x_train)

"""karena test size 0.2 maka data dikurang 2 menjadi 8"""

print(x_test)

print(y_train)

print(y_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

"""3: adalah 3 sampai akhir (karena matriks ordo 3)"""

print(x_train)

print(x_test)