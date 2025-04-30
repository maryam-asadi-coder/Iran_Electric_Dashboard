from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load data
df = pd.read_excel('data/Iran Electricity Portfolio 1967-2016(Million Kwh).xlsx')

# Clean and prepare data
df = df.rename(columns=lambda x: x.strip())
df['Year'] = df['Year'].astype(str)

# List of energy types, excluding 'Year' and 'Sum'
energy_types = [col for col in df.columns if col not in ['Year', 'Sum']]
renewable = ['Hydro', 'Solar', 'Wind', 'Bio', 'Geo', 'Tidal']
non_renewable = list(set(energy_types) - set(renewable))

# Debug: Print the lists to ensure correctness
print("Energy Types:", energy_types)
print("Renewable:", renewable)
print("Non-Renewable:", non_renewable)

@app.route('/')
def index():
    return render_template('index.html', energy_types=energy_types + ['Renewable Energy', 'Non-Renewable Energy'])

@app.route('/data/<energy_type>')
def get_energy_data(energy_type):
    try:
        # Convert energy_type to match DataFrame column case
        df_columns_lower = {col.lower(): col for col in df.columns}
        energy_type_lower = energy_type.lower()
        
        if energy_type == 'Renewable Energy':
            data = df.copy()
            data['Renewable'] = data[renewable].sum(axis=1)
            result = {'labels': data['Year'].tolist(), 'values': data['Renewable'].astype(float).tolist()}
        elif energy_type == 'Non-Renewable Energy':
            data = df.copy()
            data['NonRenewable'] = data[non_renewable].sum(axis=1)
            result = {'labels': data['Year'].tolist(), 'values': data['NonRenewable'].astype(float).tolist()}
        elif energy_type_lower in df_columns_lower:
            # Use the original column name from the DataFrame
            actual_column = df_columns_lower[energy_type_lower]
            result = {'labels': df['Year'].tolist(), 'values': df[actual_column].astype(float).fillna(0).tolist()}
        else:
            print(f"Energy type '{energy_type}' not found in DataFrame columns.")
            result = {'labels': [], 'values': []}
        return jsonify(result)
    except Exception as e:
        print(f"Error for {energy_type}: {str(e)}")
        return jsonify({'labels': [], 'values': []})

if __name__ == '__main__':
    app.run(debug=True)