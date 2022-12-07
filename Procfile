# Copied from Professor Sherriff's Example Repo, Procfile
# https://github.com/uva-cs3240-f21/Staff-Build-Example/blob/main/Procfile

# referenced this for fixing heroku crash erros
# https://stackoverflow.com/questions/28271011/django-heroku-failing-to-launch-at-error-code-h10-desc-app-crashed

release: python manage.py migrate
web: gunicorn mysite.wsgi:application --log-file - --log-level debug