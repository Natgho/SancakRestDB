#SancakMK Member Management Panel
Note: Database already exist, dont forget add "fake" tag into migration command.
python manage.py migrate --fake <appname>  
Run into server and save log file (for just only development version):
python manage.py runserver 0.0.0.0:8000 >> log.log  &