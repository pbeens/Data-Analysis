import pandas as pd

# Set file variables
csv_file = 'Data/x-y-data.csv'
html_file = 'Data/x-y-data.html'

# Read CSV file into DataFrame
df = pd.read_csv(csv_file)

# Convert DataFrame to HTML table with custom options
html_table = df.to_html(classes='table table-striped', table_id='my-table', index=False)

# Write HTML table to file
with open(html_file, 'w') as f:
    f.write(html_table)
