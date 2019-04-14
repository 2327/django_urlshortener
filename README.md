run with virtualenv:
```
   virtualenv --python=python3 .
   source bin/activate
   pip install --upgrade pip
   pip install django==2.2
   django-admin startproject urlshortener
   cd urlshortener
   django-admin startapp siteapp
   rm db.sqlite3;  ./manage.py makemigrations &&  ./manage.py migrate 

   deactivate
```
run with docker:
```   
   docker build -t url:latest .
   docker run -ti -p 8000:8000 url:latest 
```
run with docker-compose: