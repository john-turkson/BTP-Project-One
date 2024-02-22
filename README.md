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
7. Set FLASK_APP environment variable: ```set FLASK_APP=server.py``` or ```$env:FLASK_APP = "server.py"``` (depending on if you're using Command Prompt or PowerShell)
8. Run the command: flask run to start the backend server.
9. Lastly, if you want to exit the environment, you can use ```deactivate```

### Vue Frontend Initial Setup

1. Navigate into the frontend folder, then the ```music-management-app``` folder
2. Run the command ```npm install```
3. Wait for packages to load, then run the command ```npm run dev``` 
