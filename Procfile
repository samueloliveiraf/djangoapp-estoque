release: python manage.py migrate
web: gunicorn app_web.wsgi --log-file -
release: python manage.py collectstatic