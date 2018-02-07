

# Installation

`$ git clone https://github.com/bkawan/pms.git`

`$ cd pms`

`$ virtualenv -p python3 venv`

`$ source venv/bin/activate`

##### If you are on production
    `$ pip install -r requirements/dev.txt`

##### If you are on production
    `$ pip install -r requirements/prod.txt`
    
    
`$ python manage.py migrate`

###### Create a test user and company
    `$ python manage.py init`


`$ python manage.py runserver`

Go to browser and http://localhost:8000/


To login Go to http://localhost:8000/admin/login/

`username: testuser`

`password: password` 

