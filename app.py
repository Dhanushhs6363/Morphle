from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

# Endpoint for /htop
@app.route('/htop')
def htop():
  
    full_name = "Dhanush H S"  
   
    system_user = os.getenv('USER') or os.getenv('USERNAME') or "Unknown_User"

   
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Windows/Linux: Run top or tasklist depending on OS
    try:
        if os.name == 'nt':  # For Windows
            top_output = subprocess.check_output(['tasklist']).decode('utf-8')
        else:  # For Linux/Unix
            top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except subprocess.CalledProcessError as e:
        top_output = f"Error fetching system information: {str(e)}"

    
    response = f"""
    <html>
    <head><title>System Information</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>User:</strong> {system_user}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <p><strong>Top Output:</strong></p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

    return response

if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000,debug=True)