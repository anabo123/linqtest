import mysql.connector
import random
from datetime import datetime, timedelta

db_config = {
    "host": "localhost",
    "user": "linquser",
    "password": "linqpass",
    "database": "linqdb",
    "port": 3306
}

categories = ["Tech", "Finance", "Health", "Education", "Sports"]

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Clear table before inserting fresh data
    cursor.execute("DELETE FROM sample_data")
    conn.commit()

    # Generate diverse mock data
    for days_ago in range(30):  # 30 days of data
        for category in categories:
            value = round(random.uniform(10, 100), 2)

            hours = random.randint(0, 23)
            minutes = random.randint(0, 59)
            seconds = random.randint(0, 59)

            random_date = datetime.now() - timedelta(days=days_ago)
            random_date = random_date.replace(
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
            second=random.randint(0, 59),
            microsecond=0
            )
            timestamp = random_date

            cursor.execute(
                "INSERT INTO sample_data (category, value, timestamp) VALUES (%s, %s, %s)",
                (category, value, timestamp)
            )

    conn.commit()
    print("✅ Balanced data inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
