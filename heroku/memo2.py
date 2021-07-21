#if heroku is being really annoying -> heroku run python manage.py clearsessions
#git init
#heroku create
#heroku run python manage.py makemigrations
#heroku run python manage.py migrate
#git add .
#git commit -m "initial commit"
#git push heroku main
#heroku ps:scale worker=1
#heroku logs --tail
#heroku open
#heroku ps:scale worker=0

#styles aren't updating ?  
#heroku run python manage.py collectstatic
#if styles still arent loading just copy the static files manually to the staticfiles folder and replace them with the modified version 
# admin not working with heroku?

#admin isn't working with heroku ? 
#heroku run python manage.py createsuperuser
#Anyway when you have DB you need to connect your APP with DB on Heroku. For this purpose I added in settings.py:

#DATABASES = {'default': dj_database_url.config(default=‘URI of DB on Heroku’)}

#database not loading ?
#You've not set a "real" production database
#You've not used rake db:migrate in production
#heroku run rake db:migrate

#get the error only one 1 free size dynos ?
#in console run:

#heroku ps
#heroku pg
#the result is some like this:
'''
=== HEROKU_POSTGRESQL_OLIVE_URL
Plan:                  Hobby-dev
Status:                Available
Connections:           0/20
PG Version:            13.3
Created:               2021-07-18 06:00 UTC
Data Size:             8.7 MB
Tables:                12
Rows:                  60/10000 (In compliance)
Fork/Follow:           Unsupported
Rollback:              Unsupported
Continuous Protection: Off
Add-on:                postgresql-concave-19053
'''

#if rows 0/10000 then it isnt updated 
# python3 manage.py makemigrations 
# python3 manage.py migrate
#python3 manage.py migrate --run-syncdb
#outside of the heroku app
# and then recommit in heroku 


#run.4859 (Free): up 2016/01/12 21:28:41 (~ 7m ago): rails c
#So the numbers 4859 represent the session that is open and needs to be closed. To fix the error you need to run(Obviusly, replace the number 4859 by the number obtained):

#heroku ps:stop run.4859
#heroku ps:stop run.web.1
#heroku ps:stop run.worker.1

#more issues with migrations?
#just remove all the migrations out of the salonapp -> migrations folder -> and all the ones in pycache too

#issues with static files ?
#
#STATIC_URL = '/static/'

#if not DEBUG:
#STATIC_ROOT = os.path.join(BASE_DIR, "static")

#STATICFILES_DIRS = [
 #   os.path.join(BASE_DIR),
#]


'''
I faced the same problem in django 2.2, The following worked for me...

delete the migrations folder resided inside the app folder
delete the pycache folder too
restart the server [if your server is on and you are working from another cli]
python manage.py makemigrations <app_name> zero
python manage.py makemigrations <app_name> [explicit app_name is important]
python manage.py migrate

  '''
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
'''
Password for user postgres:
postgres=#
Code language: PHP (php)
Third, switch to a database e.g.., dvdrental:

postgres=# \c dvdrental
You are now connected to database "dvdrental" as user "postgres".
Code language: PHP (php)
Note that you can connect to a specific database when you log in to the PostgreSQL database server:

$ psql -U postgres -d dvdrental
In this command, -d flag means database. In this command, you connect to the dvdrental datbase using the postgres user.

Third, use the \dt command from the PostgreSQL command prompt to show tables in the dvdrental database:

postgres=# \dt
'''










#heroku run python manage.py runserver


