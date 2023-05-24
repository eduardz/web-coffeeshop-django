### Project Cafenea

#### Crearea Proiectului in VSCode
VSCode Open folder -> new terminal console:
` pip install django `
`PS C:\Users\eu\Desktop\coffeeshop> django-admin startproject cofeeshop . `

##### Setup requirements.txt
Save the requirements `pip list`;
` pip freeze > requirements.txt `

##### Pentru noi instalari modulele pip trebuie instalate
` sudo dnf install python3-pip `
`python3 -m pip install -r requirements.txt`
`pip install -r requirements.txt`

##### Start the server to create database
`PS C:\Users\eu\Desktop\coffeeshop> python manage.py runserver `
Allow from other locations: 
` python3 manage.py runserver 0.0.0.0:8000 `

##### Porneste aplicatia cu nume diferit fata de proiect
`PS C:\Users\eu\Desktop\coffeeshop> python manage.py startapp coffee `


#### Creare baza de date in cofee/models.py in cofeeshop/settings.py database -> db.sqlite3   \
#### Add app to INSTALLED_APPS (cofeeshop/settings.py) then migrate database \
` PS C:\Users\eu\Desktop\coffeeshop> python manage.py makemigrations ` 
` python manage.py migrate `

#### Backed Django
Mgrate face push la configurari in db
``` 
python manage.py migrate
```
#### create admin user
` python manage.py createsuperuser `

#### Produsele se adauga din admin interface , apoi se creaza folder nou de templates pentru web pages coffee/templates 
Se creaza home.html si base.html 
Iar in base.html  in care se adauga starter template  ->  https://getbootstrap.com/docs/4.3/getting-started/introduction/ \
Tot in base.html se adauga si navigation bar - > https://getbootstrap.com/docs/4.3/components/navbar/ \
Iar in home.html folosesc card style template  https://getbootstrap.com/docs/4.3/components/card/ 


###### Run the server to get access from all interfaces (external access to server) and forward to a reverse proxy server  
` python3 manage.py runserver 0.0.0.0:8000 `

### Server runs in docker
docker compose up -d
