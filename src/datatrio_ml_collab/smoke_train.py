import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from datatrio_ml_collab.features import add_binary_target

with open("params.yaml") as f:
    params = yaml.safe_load(f)

df = pd.read_csv("tests/data/sample.csv", header=None)
df.columns = [f"f{i}" for i in range(df.shape[1] - 1)] + ["label"]
df = add_binary_target(df).drop(columns=["label"])

train, test = train_test_split(
    df, test_size=params["split"]["test_size"], random_state=params["seed"]
)
X_train, y_train = train.drop(columns=["is_attack"]), train["is_attack"]
X_test, y_test = test.drop(columns=["is_attack"]), test["is_attack"]

prep = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), params["features"]["categorical"])],
    remainder="passthrough",
)
model = RandomForestClassifier(n_estimators=10, random_state=params["seed"])
pipe = Pipeline([("prep", prep), ("model", model)]).fit(X_train, y_train)

acc = accuracy_score(y_test, pipe.predict(X_test))
print(f"Smoke train OK, accuracy={acc:.3f}")
