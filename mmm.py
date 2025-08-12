import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load data
iris = load_iris()
X = iris.data
y = iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

st.title("🌸 Iris Flower Prediction App")

st.write("Adjust the sliders to set flower features:")

# Feature sliders
sepal_length = st.slider("Sepal length (cm)", float(X[:, 0].min()), float(X[:, 0].max()), float(X[:, 0].mean()))
sepal_width = st.slider("Sepal width (cm)", float(X[:, 1].min()), float(X[:, 1].max()), float(X[:, 1].mean()))
petal_length = st.slider("Petal length (cm)", float(X[:, 2].min()), float(X[:, 2].max()), float(X[:, 2].mean()))
petal_width = st.slider("Petal width (cm)", float(X[:, 3].min()), float(X[:, 3].max()), float(X[:, 3].mean()))

# Make prediction
input_features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_features)
predicted_class = iris.target_names[prediction[0]]

st.subheader("🌼 Predicted Iris Class:")
st.write(f"**{predicted_class}**")
