git init
heroku create
heroku run python manage.py migrate
git add .
git commit -m "initial commit"
git push heroku master
heroku ps:scale worker=1
heroku logs --tail
heroku open
heroku ps:scale worker=0
