# Hosted dashboard

This is a template for a dashboard with interactive plotting that is hosted online for remote viewing. It uses the Plotly Dash framework built on top of Flask for Python.


## Setup for development on Linux or MacOS

Install / upgrade pip: `python3 -m pip install --user --upgrade pip`

Test pip version: `python3 -m pip --version`

Install virtualenv: `python3 -m pip install --user virtualenv`

To create a virtual environment, navigate to the project folder and run: `python3 -m env <env>`, where `<env>` is the name of your new virtual environment.

Before installing packages inside the virtual environment, activate the environment: `source <env>/bin/activate`, where `<env>` is the name of your virtual environment.

To deactivate the environment: `deactivate`

Once the environment is activated, use pip to install libraries in it.

To export the list of installed packages as a `requirements.txt` file: `pip freeze > requirements.txt`

To install packages from the requirements file: `pip install -r requirements.txt`


