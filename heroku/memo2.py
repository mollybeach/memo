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
#the result is some like this:

#run.4859 (Free): up 2016/01/12 21:28:41 (~ 7m ago): rails c
#So the numbers 4859 represent the session that is open and needs to be closed. To fix the error you need to run(Obviusly, replace the number 4859 by the number obtained):

#heroku ps:stop run.4859
#or
#heroku ps:stop run.web.1
#or
#heroku ps:stop run.worker.1








#Firstly, you need to create a production db to run on Heroku. Heroku does not host any db for you - it only runs on the Amazon EC2 stack; meaning you have to either prodivde your own DB server, or use one of Heroku's postgres instances

#After you have a production database, you'll just need to run heroku run rake db:migrate from your command-line to get all your tables populated on the db server, which should resolve the error


#heroku run python manage.py runserver


