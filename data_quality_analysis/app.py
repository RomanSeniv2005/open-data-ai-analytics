import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@db:5432/mydb")

df = pd.read_sql("SELECT * FROM data", engine)

report = {
    "missing_values": df.isnull().sum().to_dict(),
    "duplicates": int(df.duplicated().sum()),
    "shape": df.shape
}

# зберігаємо звіт
pd.Series(report).to_json("/app/reports/data_quality.json")

print("Data quality analysis done!")