# django-orm-watching-storage-master
## This is the bank's security console.

## Setting environment variables
* Create `.env` file in project directory and write:
```
DB_ENGINE=REPLACE_ME
DB_HOST=REPLACE_ME
DB_PORT=REPLACE_ME
DB_NAME=REPLACE_ME
DB_USER=REPLACE_ME
DB_PASSWORD=REPLACE_ME
SECRET_KEY=REPLACE_ME
DEBUG=REPLACE_ME
ALLOWED_HOSTS=REPLACE_ME
```		
### Requirements
* django==3.2.*
* environs==9.5.0
* psycopg2-binary==2.9.*

Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```		
## Application launch

### Open project directory from cmd
```
$ python manage.py runserver 0.0.0.0:8000
```

### Run in your browser [http://127.0.0.1:8000](http://127.0.0.1:8000)

Now you can look bank's security console
![Desktop Screenshot 2022 09 09 - 21 52 47 62](https://user-images.githubusercontent.com/105148929/189380185-da54425f-cbef-4d6c-a310-bfda8b3d57a6.png)


Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
