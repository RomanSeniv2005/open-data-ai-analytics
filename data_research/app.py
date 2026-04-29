import time
import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# 🔁 retry логіка
for i in range(10):
    try:
        df = pd.read_sql("SELECT * FROM data", engine)
        print("Connected to DB and table exists!")
        break
    except Exception as e:
        print(f"Waiting for table... attempt {i+1}")
        time.sleep(3)
else:
    raise Exception("Table 'data' not found after retries")

# далі твоя логіка
print(df.head())