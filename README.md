# isms-prj
مدیریت  اسناد حهت انجام ممیزی مراقبتی

![Image of gunicorn](http://tamadon.net/python/wp-content/uploads/2020/09/Deployment-Strategy-www.tamadon.net_-768x654.jpg)

  🤗 🙂
 ##  this is a table  
 No | Name | Description |
 ---|------|-------------|
 1|ali| desc1
 2|hassan | des 2
 
- [x] ToDo 1
- [ ] Todo 2s an incomplete item
- [ ] 
 
 ```
 pip install python-decouple
 IN FILE -> myproject/settings.py
    from decouple import config
    SECRET_KEY = config('SECRET_KEY')
 CREAT FILE .env 
 add .env   to  gitignore
 
 Libogram/
 |-- Libogram/
 |    |-- accounts/
 |    |-- boards/
 |    |-- myproject/
 |    |-- static/
 |    |-- templates/
 |    |-- .env        <-- here!
 |    |-- .gitignore
 |    |-- db.sqlite3
 |    +-- manage.py
 +-- venv/
 
pip install dj-database-url
import dj_database_url
IN FILE -> myproject/settings.py
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }
pip freeze | requirements.txt
install python and postgres 
install  nginx
install  supervisor
  sudo systemctl enable supervisor
  sudo systemctl start supervisor
install virtualenv 
 adduser isms
 gpasswd -a isms sudo
 sudo su - postgres
 createuser u_isms
 createdb django_isms --owner u_isms
 psql -c "ALTER USER u_isms WITH PASSWORD 'ALzIzKAdCssHAL#$tr5d6$RGT*I2w'"
 exit
sudo su - isms
pwd
/home/ismsprj
git clone
virtualenv venv -p python3.6
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
pip install psycopg2


```
 
``` python
def add():
 return a+b
 
```
