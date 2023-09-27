# Website Monitor Service

The **Website Monitor Service** is a Python script that functions as a Windows service, periodically checking the status of a specified website. The service logs the results to a file, allowing users to monitor the availability of a website over time.

## Features

- **Website Monitoring:** The service sends HTTP requests to the specified website at regular intervals to check its availability.

- **Logging:** The results of each check, including whether the website is alive and the HTTP status code, are logged to a designated log file.

- **Windows Service:** Utilizes the `win32serviceutil` library to run as a Windows service, making it suitable for background monitoring.

## Installation

1. **Download Project:**
   - Clone the repository using Git:
     ```bash
     git clone https://github.com/nadavc25/windows_service.git
     ```

3. **Navigate to Project Directory:**
   ```bash
   cd website-monitor-service

4. **Configuration:**
   - Open the `website_monitor.py` file.
   - Replace the value of `self.url_to_monitor` with the URL of the website you want to monitor.
   - Replace the value of `self.log_file` with the desired path for the log file.

5. **Virtual Environment:**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```bash
       source venv/bin/activate
       ```

6. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt


6. **Install Service:**
    - Open a command prompt with administrator privileges.
    - Navigate to the directory containing website_monitor.py.
    
    - Run the command:
   ```bash
   python website_monitor.py install


7. **Start Service:**
    - Start the service using the Service Manager or the command:
   ```bash
   python website_monitor.py start

7. **Stop Service:**
    - Stop the service using the Service Manager or the command: 
   ```bash
   python website_monitor.py stop
