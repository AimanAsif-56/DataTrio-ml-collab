import sys

import pandas as pd

df = pd.read_csv("tests/data/sample.csv", header=None)
errors = []

# Schema
if df.shape[1] != 42:
    errors.append(f"Expected 42 columns, got {df.shape[1]}")

# Null counts
if df.isna().sum().sum() > 0:
    errors.append("Dataset contains null values")

# Value ranges
if not set(df[1].unique()) <= {"tcp", "udp", "icmp"}:
    errors.append("Unexpected protocol_type values")
if (df[[0, 4, 5]] < 0).any().any():
    errors.append("Negative duration/src_bytes/dst_bytes")
rate_cols = list(range(24, 31)) + list(range(33, 41))
if ((df[rate_cols] < 0) | (df[rate_cols] > 1)).any().any():
    errors.append("Rate columns outside [0, 1]")
if not df[41].astype(str).str.endswith(".").all():
    errors.append("Label format unexpected")

if errors:
    print("DATA CHECK FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("Data checks passed")
