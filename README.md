
Iran Electric Dashboard
-----------
Overview
The Iran Electric Dashboard is a Python-based web application designed to visualize the energy consumption and generation portfolio of Iran from 1967 to 2020. This dashboard provides an interactive and informative visualization of the energy mix used in Iran, showcasing various energy sources such as steam, gas, hydro, solar, wind, nuclear, and more.

Technologies Used
-----------
Flask 2: Web framework for the backend.

Pandas: For data manipulation and analysis.

Plotly: For interactive charting and data visualization.

Openpyxl: For reading and writing Excel files.

Chart.js: JavaScript library used for chart rendering.

Features
-----------
Energy Data Visualization: Interactive charts displaying the electricity generation data for each energy type (e.g., Steam, Gas, Wind, Solar).

Time Series Data: Displays data from the year 1346 (1967) to 1395 (2016) for various energy sources.

Dynamic Updates: The chart updates dynamically when the user selects a different energy source.

Background Video: Enhances the user experience with a background video that highlights the theme of energy and the environment.

Installation
------------
Prerequisites
Make sure you have Python 3.x installed on your system. You will also need to install the following dependencies:
pip install Flask pandas plotly openpyxl
Running the Application
1.Clone this repository to your local machine:
git clone https://github.com/yourusername/Iran_Electric_Dashboard.git
cd Iran_Electric_Dashboard
2.Run the Flask server:
python app.py
3.Open your browser and go to http://127.0.0.1:5000 to view the dashboard.

File Structure
-------------
Iran_Electric_Dashboard/
│
├── app.py                # Main Flask application file
├── templates/
│   ├── index.html        # HTML for the dashboard
│   └── layout.html       # Base HTML layout
├── static/
│   ├── video/            # Background video folder
│   │   └── background.mp4
│   ├── css/              # Stylesheets for custom styles
│   └── js/               # JavaScript for handling chart updates
├── data/                 # Directory for storing energy data
│   └── energy_data.xlsx  # Energy generation data
└── README.md             # Project documentation

Data
-----------
The dataset used in this dashboard contains yearly data on energy generation from 1967 to 2016, including different energy sources like:

Steam

Gas

Combined Cycle

Diesel

Hydro

Nuclear

Solar

Wind

Bio

Geothermal

Tidal

The data is stored in an Excel file (energy_data.xlsx) that is read by the backend to generate dynamic charts.

How It Works
------------
Data Handling: The energy data is loaded using Pandas, and each energy source is represented as a separate dataset.

Chart Updates: Users can select an energy type (e.g., Steam, Solar, Wind), and the app dynamically fetches the corresponding data to update the chart.

Backend: Flask serves the data and handles API requests to fetch energy data for different years and energy types.

Acknowledgments
-------------
Flask for providing a lightweight web framework.

Plotly for creating powerful interactive charts.

Chart.js for interactive chart rendering.

