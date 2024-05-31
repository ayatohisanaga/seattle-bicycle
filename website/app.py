from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os
import json

app = Flask(__name__)

# Load metadata from the JSON file
with open("outputs/metadata.json", "r") as file:
    metadata = json.load(file)

# Path to the directory with the merged datasets
merged_data_directory = 'website/datasets'

# Load all merged datasets into a dictionary
merged_data = {}
for file in os.listdir(merged_data_directory):
    if file.endswith('_merged.csv'):
        location_name = file.replace('_merged.csv', '')
        df = pd.read_csv(os.path.join(merged_data_directory, file))
        merged_data[location_name] = df

@app.route('/')
def index():
    return render_template('map.html', locations=metadata)

@app.route('/select_dates', methods=['GET', 'POST'])
def select_dates():
    if request.method == 'GET':
        location_name = request.args.get('location')
        # Find the metadata for the selected location
        location_data = next((item for item in metadata if item['identifier'] == location_name), None)
        if location_data:
            start_date = location_data['date_range']['start']
            end_date = location_data['date_range']['end']
            return render_template('select_dates.html', location=location_name, start_date=start_date, end_date=end_date)
        else:
            return redirect(url_for('index'))
    elif request.method == 'POST':
        location_name = request.form['location']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        # Convert dates to datetime for comparison
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        
        # Filter the dataset based on the selected location and date range
        selected_data = merged_data[location_name][(pd.to_datetime(merged_data[location_name]['date']) >= start_date) & (pd.to_datetime(merged_data[location_name]['date']) <= end_date)]
        
        # Ensure selected_data is a DataFrame
        selected_data = pd.DataFrame(selected_data)
        
        return render_template('display_data.html', location=location_name, data=selected_data)

import tempfile

def convert_to_metric(data):
    # Convert temperature columns to Celsius
    data['temp_min'] = (data['temp_min'] - 32) * 5 / 9
    data['temp_max'] = (data['temp_max'] - 32) * 5 / 9
    data['temp_avg'] = (data['temp_avg'] - 32) * 5 / 9

    # Convert precipitation columns to millimeters
    data['precipitation'] *= 25.4  # 1 inch = 25.4 millimeters

    # Convert wind speed columns to kilometers per hour
    data['wind_speed_avg'] *= 1.60934  # 1 mile per hour = 1.60934 kilometers per hour

    return data

@app.route('/download_data/<location>/<unit_system>', methods=['GET'])
def download_data(location, unit_system):
    # Retrieve the selected data based on the location
    selected_data = merged_data.get(location)
    if selected_data is None:
        return "Data not found for the specified location.", 404

    # Get the date range from the query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date and end_date:
        # Convert dates to datetime for comparison
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter the dataset based on the date range
        selected_data = selected_data[(pd.to_datetime(selected_data['date']) >= start_date) & (pd.to_datetime(selected_data['date']) <= end_date)]

    # Convert units if necessary
    if unit_system == 'metric':
        # Convert selected_data to metric units
        selected_data = convert_to_metric(selected_data)

    # Round all numeric columns to 2 decimal places
    selected_data = selected_data.round(2)

    # Create a temporary file to store the CSV data
    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp_file:
        # Write the CSV data to the temporary file
        selected_data.to_csv(temp_file.name, index=False)

    # Prepare response with the file attachment
    return send_file(temp_file.name, mimetype='text/csv', as_attachment=True, download_name=f"{location}_data.csv")

if __name__ == '__main__':
    app.run(debug=True)
