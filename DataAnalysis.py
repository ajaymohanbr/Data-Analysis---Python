import pandas as pd
import plotly.express as px

table = pd.read_csv('telecom_users.csv')

# To drop an unwanted column
table = table.drop('Unnamed: 0', axis=1)

# To convert the column TotalGastos to numeric

table['TotalGasto'] = pd.to_numeric(table['TotalGasto'], errors="coerce")

# To solve Nan

table = table.dropna(how='all', axis=1)
table = table.dropna(how='any', axis=0)

print(table["Churn"].value_counts(normalize=True).map('{:.2%}'.format))

# Create graph
for column in table.columns:
    graph = px.histogram(table, x=column, color="Churn", text_auto=True)
# Show graph
    graph.show()