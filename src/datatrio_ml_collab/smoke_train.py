import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

COLUMN_NAMES = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot",
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",
    "srv_count",
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",
    "dst_host_same_srv_rate",
    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",
    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    "label",
]

with open("params.yaml") as f:
    params = yaml.safe_load(f)

df = pd.read_csv("tests/data/sample.csv", header=None, names=COLUMN_NAMES)
df["is_attack"] = (df["label"] != "normal.").astype(int)
df = df.drop(columns=["label"])

train, test = train_test_split(
    df,
    test_size=params["split"]["test_size"],
    random_state=params["seed"],
    stratify=df["is_attack"],
)

X_train = train.drop(columns=["is_attack"])
y_train = train["is_attack"]
X_test = test.drop(columns=["is_attack"])
y_test = test["is_attack"]

categorical_columns = ["protocol_type", "service", "flag"]

prep = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)],
    remainder="passthrough",
)

model = RandomForestClassifier(n_estimators=10, random_state=params["seed"])

pipe = Pipeline([("prep", prep), ("model", model)]).fit(X_train, y_train)

acc = accuracy_score(y_test, pipe.predict(X_test))
print(f"Smoke train OK, accuracy={acc:.3f}")
