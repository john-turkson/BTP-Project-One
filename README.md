
# BTP-Project-One

## Music Library Management System

### Flask Backend Initial Setup

1. Navigate into the backend folder
2. Once the packages have been installed, create a virtual environment with this command 
	```py -3 -m venv <name of enviornment>``` or ```python -m venv <name of environment>``` (depending on what version of python you have)

3. Once this command is complete, you should see an env (or a folder named after whatever you have chosen for the name) folder in your backend folder.
4. To switch into the virtual environment: ```<name of enviornment>\Scripts\activate```
5. Once in the virtual environment, your terminal should look like this: ```(env) C:\Users\jturk\Documents\Seneca\BSD\BTP405\Project One\BTP-Project-One\backend>```
6. Run this command when inside the virtual environment and in the backend folder:  ```pip install -r requirements.txt```
7. Set FLASK_APP environment variable: ```set FLASK_APP=app.py``` or ```$env:FLASK_APP = "app.py"``` (depending on if you're using Command Prompt or PowerShell)
8. Run the command: flask run to start the backend server.
9. Lastly, if you want to exit the environment, you can use ```deactivate```

### Vue Frontend Initial Setup

1. Navigate into the frontend folder, then the ```music-management-app``` folder
2. Run the command ```npm install```
3. Wait for packages to load, then run the command ```npm run dev``` 

### Setting up PostgreSQL
1. Head over to PostgreSQL's website and download their installer for your operating system. [Installer](https://www.postgresql.org/download/)
2. Follow the installer wizard and install PostgreSQL.
3. Add PostgreSQL's bin directory to the PATH environment variable:
	- Find your file path (ex: C:\Program Files\PostgreSQL\16\bin).
	- Use the win + r shortcut to bring up the Run dialog and enter ```sysdm.cpl```.
	- Select the Advanced tab at the top and click the ```Environment Variables``` button at the bottom.
	- In environment variables you want to use the bottom section that says ```System```.
	- Under ```System``` you want to find the ```Path``` variable and click on the ```Edit``` button.
	- Once ```Edit``` is clicked you can click ```New``` and add your bin path ```C:\Program Files\PostgreSQL\16\bin``` to the environment variable.
	- Finally you can now click ```Ok``` on every box and you should be able to use PostgreSQL in CMD. 
