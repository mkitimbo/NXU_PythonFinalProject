<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Income Survey Tool - Final Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        h3 {
            color: #34495e;
        }
        pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin-bottom: 10px;
        }
        code {
            background-color: #ecf0f1;
            padding: 2px 4px;
            border-radius: 4px;
        }
        a {
            color: #2980b9;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1>Income Survey Tool - Final Project</h1>

    <p>This project is a web-based survey tool designed to collect participants' data on income and expenses. It was developed using <strong>Flask</strong> for the web framework, <strong>MongoDB</strong> for data storage, and <strong>Python</strong> for data processing and analysis. The project aims to help analyze income spending patterns in preparation for a new product launch in the healthcare industry.</p>

    <h2>Overview</h2>
    <ul>
        <li><strong>Web Development:</strong> Flask application to collect survey data.</li>
        <li><strong>Data Storage:</strong> MongoDB (Atlas) for storing user details and expenses.</li>
        <li><strong>Data Processing:</strong> Python for CSV export and analysis.</li>
        <li><strong>Data Visualization:</strong> Charts generated with <strong>Matplotlib</strong> and <strong>Seaborn</strong>.</li>
        <li><strong>Deployment:</strong> Hosted on <strong>Render</strong> (AWS-like environment).</li>
    </ul>

    <h2>Project Structure</h2>
    <pre>
/PythonFinalProj
    /app
        /templates
            index.html          # Survey form template
        /static
            /images
                age_income_chart.png      # Age vs Income Chart
                gender_spending_chart.png # Gender Distribution Chart
        __init__.py                # Initialize Flask app and MongoDB
        models.py                  # User model class for data processing
        routes.py                  # Routes for handling the survey and MongoDB logic
    /data
        users.csv                   # CSV file storing user survey responses
    run.py                         # Entry point to run the Flask app
    requirements.txt               # Required Python libraries
    README.md                      # Project documentation
    </pre>

    <h2>Prerequisites</h2>
    <ul>
        <li><strong>Python:</strong> 3.x</li>
        <li><strong>Flask:</strong> Web framework for Python.</li>
        <li><strong>Flask-PyMongo:</strong> MongoDB integration for Flask.</li>
        <li><strong>Matplotlib & Seaborn:</strong> For generating data visualizations.</li>
        <li><strong>pandas:</strong> For handling and processing data.</li>
        <li><strong>MongoDB Atlas:</strong> Cloud MongoDB for storing survey responses.</li>
    </ul>

    <p>To install the necessary dependencies, run:</p>
    <pre>
pip install -r requirements.txt
    </pre>

    <h2>Setup Instructions</h2>
    <h3>Step 1: Clone the Repository</h3>
    <p>Clone the project repository to your GitHub account:</p>
    <pre>
git clone https://github.com/yourusername/PythonFinalProj.git
cd PythonFinalProj
    </pre>

    <h3>Step 2: Set Up MongoDB</h3>
    <p>Create a <strong>MongoDB Atlas</strong> account and create a new cluster. Retrieve the <strong>MongoDB connection string</strong> and configure it in the <code>__init__.py</code> file.</p>

    <h3>Step 3: Run the Flask App Locally</h3>
    <p>Run the Flask app locally by executing the following:</p>
    <pre>
python run.py
    </pre>
    <p>The application will be available at <strong>http://localhost:5000</strong>.</p>

    <h3>Step 4: Deploy on Render (or AWS)</h3>
    <p>For deployment, follow the instructions on the <a href="https://render.com/docs/deploy-flask" target="_blank">Render Deployment Docs</a> or host it on any other platform like AWS or Heroku. The application is hosted at:</p>
    <p><strong><a href="https://pythonfinalproj.onrender.com" target="_blank">https://pythonfinalproj.onrender.com</a></strong></p>

    <h3>Step 5: Usage</h3>
    <ol>
        <li>Open the survey form at <strong><a href="https://pythonfinalproj.onrender.com" target="_blank">https://pythonfinalproj.onrender.com</a></strong>.</li>
        <li>Fill in your details (Age, Gender, Income, and Expenses).</li>
        <li>Submit the form. The data will be stored in MongoDB and exported to a CSV file.</li>
    </ol>

    <h3>Step 6: Data Analysis (Optional)</h3>
    <p>After collecting sufficient data, you can analyze the CSV file located in the <code>/data</code> folder. Use the <code>analysis.py</code> script to generate visualizations and insights about income distribution and spending patterns. The generated charts are saved as PNG files in the <code>/static/images</code> directory.</p>

    <h2>Files Description</h2>
    <ul>
        <li><code>__init__.py</code>: This file sets up the Flask app and connects to MongoDB via <strong>Flask-PyMongo</strong>.</li>
        <li><code>models.py</code>: Contains the <strong>User</strong> class that handles data parsing from the survey form and converts it into a dictionary format. It also handles saving the data into a CSV file.</li>
        <li><code>routes.py</code>: Defines the routes for rendering the survey form, processing the survey submissions, and interacting with MongoDB.</li>
        <li><code>run.py</code>: The entry point for running the Flask application. It initializes the app and starts the development server.</li>
        <li><code>index.html</code>: A simple HTML form for the survey, where participants can enter their details and expenses.</li>
        <li><code>analysis.py</code>: Python script for performing data analysis and generating charts. It uses <strong>pandas</strong> to load the CSV file and <strong>Matplotlib/Seaborn</strong> to generate and save visualizations.</li>
        <li><code>users.csv</code>: Stores survey responses in a CSV format, including the participant’s age, gender, income, and expenses.</li>
    </ul>

    <h2>Data Analysis</h2>
    <p>The <code>analysis.py</code> script generates the following charts:</p>
    <ul>
        <li><strong>Ages with Highest Income:</strong> A bar chart that shows the relationship between age and income.</li>
        <li><strong>Gender Distribution Across Spending Categories:</strong> A box plot displaying how male and female participants distribute their expenses across different categories (e.g., utilities, entertainment, etc.).</li>
    </ul>

    <h2>Deployment Information</h2>
    <ul>
        <li><strong>Live URL:</strong> <a href="https://pythonfinalproj.onrender.com" target="_blank">https://pythonfinalproj.onrender.com</a></li>
        <li><strong>MongoDB Connection URI:</strong> The MongoDB URI is stored as an environment variable on Render.</li>
    </ul>

    <h2>Conclusion</h2>
    <p>This project serves as a basic survey tool for collecting and analyzing data related to income and spending habits. It is designed to scale and can be easily adapted for other data collection purposes. The collected data can be visualized and exported for further analysis and business insights.</p>

    <h2>Future Enhancements</h2>
    <ul>
        <li>Add user authentication for secure access to survey data.</li>
        <li>Implement more detailed data analysis and reports.</li>
        <li>Add the ability to download a CSV file containing survey results directly from the web interface.</li>
    </ul>

    <hr>
    <p><strong>Note:</strong> For any issues or questions, feel free to open an issue in the GitHub repository or contact the project owner directly.</p>

</body>
</html>
