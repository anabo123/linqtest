import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Database connection
db_url = "mysql+pymysql://linquser:linqpass@localhost:3306/linqdb"
engine = create_engine(db_url)

query = """
SELECT category, value, DATE_FORMAT(timestamp, '%%Y-%%m-%%d %%H:%%i:%%s') as timestamp
FROM sample_data
"""
df = pd.read_sql(query, engine)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
df['value'] = pd.to_numeric(df['value'], errors='coerce')

# Drop NaNs & sort
df = df.dropna(subset=['timestamp', 'value'])
df = df.sort_values(by="timestamp")

# Get date range
min_date = df['timestamp'].min()
max_date = df['timestamp'].max()

# Create line chart for interactive viewing
fig_line = px.line(
    df,
    x="timestamp",
    y="value",
    color="category",
    title="Values Over Time by Category",
    markers=True
)

# Style for screenshot
fig_line.update_traces(marker=dict(size=6), line=dict(width=3))
fig_line.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(size=14),
    xaxis=dict(
        type="date",
        tickformat="%Y-%m-%d",
        tickangle=-45,
        range=[min_date, max_date]
    ),
    yaxis=dict(rangemode="tozero")
)

# Show interactively (screenshot this window)
fig_line.show()
