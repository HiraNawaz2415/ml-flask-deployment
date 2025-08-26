import pickle
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def main():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)

    # Ensure output folder exists
    Path("model").mkdir(parents=True, exist_ok=True)
    with open("model/model.pkl", "wb") as f:
        pickle.dump(clf, f)

    print("✅ Model trained and saved to model/model.pkl")

if __name__ == "__main__":
    main()
