import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
)

flower_data = load_iris()
df_x = pd.DataFrame(flower_data.data, columns=flower_data.feature_names)
s_y = pd.Series(flower_data.target)

print("Iris dataset loaded!")
print("Shape:", df_x.shape)
print("\nSample rows:")
print(df_x.head())
print("\nClasses:", flower_data.target_names)

train_x, test_x, train_y, test_y = train_test_split(
    df_x,
    s_y,
    test_size=0.20,
    random_state=42,
    stratify=s_y,
)

print("\nTrain count:", train_x.shape[0])
print("Test count:", test_x.shape[0])

gnb_model = GaussianNB()
gnb_model.fit(train_x, train_y)
print("\nModel training complete!")

y_hat = gnb_model.predict(test_x)

model_acc = accuracy_score(test_y, y_hat)
prec_score = precision_score(test_y, y_hat, average="weighted")
rec_score = recall_score(test_y, y_hat, average="weighted")

print("\nAccuracy:", round(model_acc * 100, 2), "%")
print("Precision (weighted):", round(prec_score, 4))
print("Recall (weighted):", round(rec_score, 4))

matrix_cm = confusion_matrix(test_y, y_hat)
print("\nConfusion Matrix:")
print(matrix_cm)

plt.figure(figsize=(6, 4))
sns.heatmap(
    matrix_cm,
    annot=True,
    fmt="d",
    cmap="Greens",
    xticklabels=flower_data.target_names,
    yticklabels=flower_data.target_names,
)
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.title("Confusion Matrix Heatmap - Iris")
plt.tight_layout()
plt.show()

print("\nClassification Report:")
print(
    classification_report(
        test_y,
        y_hat,
        target_names=flower_data.target_names,
    )
)
