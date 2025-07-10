import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target


df = pd.get_dummies(df, columns=["species"])

x = df.drop("petal length (cm)", axis=1)
y = df["petal length (cm)"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f"테스트 평균 제곱 오차 : {mse:3f}")


import streamlit as st

st.title("붓꽃 꽃잎 길이 예측기")
st.markdown("그냥 알아서 잘 하세요")

sepal_length = st.slider("꽃받침 길이", 4.0, 100.0, 5.1)
sepal_width = st.slider("꽃받침 너비", 2.0, 4.5, 3.5)
petal_width = st.slider("꽃잎 너비", 0.1, 2.5, 0.2)
species_name = st.selectbox("종", ["세토사", "버지컬러", "버지니카"])

species_index = ["세토사", "버지컬러", "버지니카"].index(species_name)
species_vector = [1 if i == species_index else 0 for i in range(3)]

if st.button("예측하기"):
    input_data = [[sepal_length, sepal_width, petal_width] + species_vector]
    input_df = pd.DataFrame(input_data, columns=[
        'sepal length (cm)', 'sepal width (cm)' , 'petal width (cm)',
        'species_0', 'species_1', 'species_2'
    ])

    prediction = model.predict(input_df)[0]
    st.success(f"예측된 꽃잎 길이는 {prediction:2f}cm 입니다")
