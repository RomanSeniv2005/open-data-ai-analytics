import pandas as pd
from sqlalchemy import create_engine

# читаємо CSV
df = pd.read_csv(
    "/app/data/raw/reestrtz01.01.2026.csv",
    sep=";",
    encoding="utf-8",
    on_bad_lines="skip"
)

# підключення до БД
engine = create_engine("postgresql://user:password@db:5432/mydb")

# запис в БД
df.to_sql("data", engine, if_exists="replace", index=False)

print("Data loaded successfully!")