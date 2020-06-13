# Hosted dashboard

This is a template for a dashboard with interactive plotting that is hosted online for remote viewing. It uses the Plotly Dash framework built on top of Flask for Python.

## Testing locally

To test locally: `python app.py`. This will open the Dash page at the localhost: `http://127.0.0.1:8050/`

To stop running the application, use `ctrl + c`


## File description

* **app.py**: Main Python file which creates the dashboard application
* **stylesheet.css**: CSS stylesheet which is called by **app.py** for styling the dashboard
* **tests.ipynb**: Jupyter notebook for testing basic data operations
* **requirements.txt**: Requirements file for installing app dependencies with pip. This is also used by the application host
* **Procfile**: file which Heroku uses to launch app
* **runtime.txt**: file which Heroku uses to determine which Python runtime version to use
 




## Setup for development on Linux or MacOS


### Setup virtual development environment

Install / upgrade pip: `python3 -m pip install --user --upgrade pip`

Test pip version: `python3 -m pip --version`

Install virtualenv: `python3 -m pip install --user virtualenv`

To create a virtual environment, navigate to the project folder and run: `python3 -m env <env>`, where `<env>` is the name of your new virtual environment.

Before installing packages inside the virtual environment, activate the environment: `source <env>/bin/activate`, where `<env>` is the name of your virtual environment.

To deactivate the environment: `deactivate`

Once the environment is activated, use pip to install libraries in it.

To export the list of installed packages as a `requirements.txt` file: `pip freeze > requirements.txt`

To install packages from the requirements file: `pip install -r requirements.txt`


### Use Git to commit to Heroku

* Setup account on Heroku and download Heroku CLI utility
* Navigate to project folder
* Commit this folder to Git
* Run `heroku login` and type in your Heroku account credentials
* Run `heroku create -n [YOUR-APP-NAME]` where YOUR-APP-NAME refers to the title of your Dash app
* `heroku git:remote -a [YOUR-APP-GIT-URL]` where YOUR-APP-GIT-URL refers to the Git link returned by 5.
* Run `git push heroku master` to deploy your app to Heroku
* `heroku ps:scale web=1` will create a Dyno and make your app live
* If you want to make changes to your app repeat steps 2. 3. and 7.
