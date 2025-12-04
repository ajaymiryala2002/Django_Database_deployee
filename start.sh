
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn django_db_curd.wsgi:application --bind 0.0.0.0:$PORT
