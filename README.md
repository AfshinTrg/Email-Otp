```
source venv/bin/activate
pip install -r requirements.txt
mv .env-sample .env
fill .env
cd emailotp/
./manage.py createsuperuser
./manage.py runserver
```
