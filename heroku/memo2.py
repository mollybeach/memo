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

python manage.py makemigrations <app_name> [explicit app_name is important]
python manage.py migrate

  '''
  
  
  '''
  Like pull but in reverse, pg:push will push data from a local database into 
a remote Heroku Postgres database. The command looks like this:

$ heroku pg:push mylocaldb HEROKU_POSTGRESQL_COLOR --app nameofapponheroku
$ heroku pg:push salon_db HEROKU_POSTGRESQL_OLIVE --app madeleinecoiffure

This command will take the local database “mylocaldb” and push it to the 
database at DATABASE_URL on the app “sushi”. In order to prevent accidental 
data overwrites and loss, the remote database must be empty. You will be 
prompted to pg:reset an already a remote database that is not empty.

Usage of the PGUSER and PGPASSWORD for your local database is also supported
for pg:push, just like for the pg:pull commands.


  PGUSER=postgres PGPASSWORD=password heroku pg:pull HEROKU_POSTGRESQL_COLOR salon_db --app nameofapponheroku
  
  PGUSER=postgres PGPASSWORD=jeannette487547 heroku pg:pull HEROKU_POSTGRESQL_OLIVE salon_db --app madeleinecoiffure
  '''
  
  
  
  
  

#print heroku database tables in terminal 
#heroku psql
'''
madeleinecoiffure::DATABASE->
madeleinecoiffure::DATABASE-> \dt
                      List of relations
 Schema |            Name            | Type  |     Owner      
--------+----------------------------+-------+----------------
 public | auth_group                 | table | kslmuwaiouqmwl
 public | auth_group_permissions     | table | kslmuwaiouqmwl
 public | auth_permission            | table | kslmuwaiouqmwl
 public | auth_user                  | table | kslmuwaiouqmwl
 public | auth_user_groups           | table | kslmuwaiouqmwl
 public | auth_user_user_permissions | table | kslmuwaiouqmwl
 public | django_admin_log           | table | kslmuwaiouqmwl
 public | django_content_type        | table | kslmuwaiouqmwl
 public | django_migrations          | table | kslmuwaiouqmwl
 public | django_session             | table | kslmuwaiouqmwl
 public | salonapp_client            | table | kslmuwaiouqmwl
 public | salonapp_feature           | table | kslmuwaiouqmwl
(12 rows)


use \q command and press enter to exit psql.



  

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

Debugger listening on ws://127.0.0.1:50144/07a77bc2-1361-4fd2-87e8-0639aff52835
For help, see: https://nodejs.org/en/docs/inspector
Debugger attached.
Creating heroku-postgresql:hobby-dev on ⬢ madeleinecoiffure... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-symmetrical-13357 as HEROKU_POSTGRESQL_MAROON_URL

'''


#Create NEW HEROKU DATABASE FROM TERMINAL
#heroku addons:create heroku-postgresql:hobby-dev
#$Created postgresql-symmetrical-13357 as HEROKU_POSTGRESQL_MAROON_URL

#MAKE MAIN DATABASE
#heroku pg:promote HEROKU_POSTGRESQL_MAROON 

#heroku pg:push salon_db HEROKU_POSTGRESQL_MAROON --app madeleinecoiffure

#heroku-cli: Pushing salon_db ---> postgresql-symmetrical-13357
#pg_dump: last built-in OID is 16383
#heroku run python manage.py runserver


