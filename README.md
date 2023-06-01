# The_Timer_Project

## How to run the code - 
To run the code for the Employee Activity Tracker project, you can follow these steps:

## Set up the development environment:

- Install Python: Download and install the latest version of Python from the official Python website (https://www.python.org).
- Install Django: Open a command prompt or terminal and run the command pip install Django to install Django framework.

## Clone the project repository:
- Create a new directory for your project.
- Open a command prompt or terminal in the newly created directory.
- Run the command git clone <repository_url> to clone the project repository. Alternatively, you can download the project as a ZIP file from the repository's webpage and extract it into your project directory.

## Navigate to the project directory:

Open a command prompt or terminal and navigate to the project directory using the cd command.

## Set up the database:

- Open the settings.py file located in the project's main directory.
- Configure the database settings according to your needs. By default, the project uses SQLite as the database, which is suitable for development purposes.
- Run the following command to create the necessary database tables: 
- Python manage.py migrations
- python manage.py migrate.

## Run the development server:

- In the command prompt or terminal, run the command -
 - python manage.py runserver.

The development server will start, and you will see output indicating that the server is running.
Open your web browser and visit http://localhost:8000 to access the Employee Activity Tracker.
Interact with the application:

Log in using your credentials or the account you just created.
Once logged in, the timer will start automatically, tracking the time you spend on the application.
To log out, click on the "Logout" button. You will see a pop-up notification displaying the login and logout times.
The time spent will be recorded in the database for evaluation purposes.
That's it! You have successfully set up and run the Employee Activity Tracker project. Feel free to explore and customize the code to fit your specific requirements.


## References:
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- HTML, CSS, and JavaScript Documentation: https://developer.mozilla.org/
