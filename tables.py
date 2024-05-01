import nbformat
import pandas as pd

def extract_tables(penguins):
    # Load the notebook
    with open('penguins.ipynb', 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Counter for table files
    table_count = 0
    
    # Iterate through each cell in the notebook
    for cell in nb['cells']:
        # Check if the cell type is code
        if cell['cell_type'] == 'code':
            # Check if the cell has any outputs
            if 'outputs' in cell:
                # Iterate through each output in the cell
                for output in cell['outputs']:
                    # Check if the output contains HTML data
                    if 'data' in output and 'text/html' in output['data']:
                        # Extract HTML table from output
                        html_table = output['data']['text/html']
                        # Convert HTML table to DataFrame
                        tables = pd.read_html(html_table)
                        # Export each table to Excel
                        for table in tables:
                            table.to_excel(f'table_{table_count}.xlsx', index=False)
                            table_count += 1

# Call the function with the path to your notebook file
extract_tables('penguins.ipynb')
