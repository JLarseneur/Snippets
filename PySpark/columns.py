## Deal with multiple columns that have have the same name
df.toDF(*[f"{col}_{i}" for i, col in enumerate(df.columns)])
