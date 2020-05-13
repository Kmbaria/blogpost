
# Blog post

# Author

by George K Mbaria

## Description

Blog It is a web application that is meant for users to add any blog post on different categories and one can get likes or comments.

The Blog It web application is meant for users to post pitches on any of the 7 different categories. These categories are:




## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between sign up and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app Blog based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments template with your comment and other comments |

## Set-up and Installation

### Prerequiites

    - Python 3.6
    - Ubuntu software

### Create a Virtual Environment

Run the following commands in the same terminal:

```sudo apt-get install python3.6-venv```

```python3.6 -m venv virtual```

```source virtual/bin/activate```

### Install dependancies

Install dependancies that will create an environment for the app to run

```pip3 install -r requirements```

Install [Postgres](https://www.postgresql.org/download/)

### Prepare environment variables

```export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchperfect'```

```export SECRET_KEY='Your secret key'```

### Run Database Migrations

```python manage.py db init```

```python manage.py db migrate -m "initial migration"```

```python manage.py db upgrade```



### Running the app in development

In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs
 No bugs

SQLAlchemy errors, automatic sign out has a short time span, deployment to heroku

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql


## Support and contact details

Contact me on Kmbaria.george@gmail.com for any comments, reviews or advice.

### License

    **MIT LICENSE**
&copy; Copyright 2020 **Jojik.GK**
