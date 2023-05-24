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


### Creare baza de date in cafeneaweb/models.py  -> in cafenea/settings.py database -> db.sqlite3
### Add app to INSTALLED_APPS (cofeeshop/settings.py) then migrate database
` PS C:\Users\eu\Desktop\coffeeshop> python manage.py makemigrations ` 


#### Backed Django
#### -> migrarea face push la configurari in db
#### create admin user
``` 
python manage.py migrate
python manage.py createsuperuser 
```
admin:pwd123 

#### Produsele se adauga din admin interface , apoi se creaza folder nou de templates pentru web pages coffee/templates 
Se creaza home.html si base.html 
Iar in base.html  in care se adauga starter template  ->  https://getbootstrap.com/docs/4.3/getting-started/introduction/ 
Tot in base.html se adauga si navigation bar - > https://getbootstrap.com/docs/4.3/components/navbar/ 
Iar in home.html folosesc card style template  https://getbootstrap.com/docs/4.3/components/card/ 


##### run the server 
` python3 manage.py runserver 0.0.0.0:8000 `



