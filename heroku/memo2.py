#git init
#heroku create
#heroku run python manage.py migrate
#git add .
#git commit -m "initial commit"
#git push heroku main
#heroku ps:scale worker=1
#heroku logs --tail
#heroku open
#heroku ps:scale worker=0
#collect static 
#heroku run python manage.py collectstatic
# admin not working with heroku?
#heroku run python manage.py createsuperuser
#Anyway when you have DB you need to connect your APP with DB on Heroku. For this purpose I added in settings.py:

#DATABASES = {'default': dj_database_url.config(default=‘URI of DB on Heroku’)}
