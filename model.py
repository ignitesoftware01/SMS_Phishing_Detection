import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('url_spam_classification.csv')
df['is_spam'] = df['is_spam'].astype(int)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['url'])
y = df['is_spam']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


def predict_spam(url):
    url_vector = vectorizer.transform([url])
    prediction = model.predict(url_vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"
