# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: datatrio-ml-collab (3.10.20)
#     language: python
#     name: python3
# ---

# %%
import sys

sys.path.insert(0, "../src")
import pandas as pd

from datatrio_ml_collab.features import add_binary_target

# %%
df = pd.read_csv("../data/raw/kddcup.csv", header=None)
df = df.rename(columns={df.columns[-1]: "label"})
df = add_binary_target(df)

# %%
# Dataset overview
print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isna().sum())
