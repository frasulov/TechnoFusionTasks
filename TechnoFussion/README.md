# Hi, I am Fagan Rasulov.


##### I have used Django (Python) for this project. Also, I have used redis server for asynchronous tasks. When we create Labels, number of labels can be thousands or more.Therefore, I create each Label asynchronously by the help of celery libarary of python and redis server.


#### You need to have redis-server in localhost, and postgress server. You can find redis and postgress settings in settings.py file.


### run following commands

(following 2 commands will create tables in db)
* python manage.py makemigrations
* python manage.py migrate

* python manage.py runserver (will run the server. default port is 8000)

Another terminal

* run redis server. (redis-server)

Another terminal

* celery -A TechnoFussion worker -l info


Enable environment before running python and celery commands.
* source venv/bin/activate  (for running python environment)


#### Note: it is not gonna work without redis server and running celery command.
