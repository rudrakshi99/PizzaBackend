# PizzaBackend
An API interface that lists the information about all the different stored pizzas, and also be able to interact with that information (such as edit or delete).

Database is able to store information about Pizza, following are the details :

* A Pizza can be of multiple types : Regular or Square
* A Pizza can be of multiple sizes : Small, Medium, Large, etc.
* A Pizza can consist of many toppings out of the following (Onion, Tomato, Corn, Capsicum, Cheese, Jalapeno etc.)

## Features :

* It is capable of receiving the posted pizza details from the frontend and store them in a database.

* It is capable of fetching the list of pizzas from the database and send them to the frontend.

* It is capable of updating the valid pizzas details in the database and send them to the frontend.

* It is capable of deleting the exixting pizza from the backend.

* It is capable of filtering the pizza based on choices.

## Technology Stack to be used:

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img 
src="https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white"/> 
<img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/>
<img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> 
<img src="https://img.shields.io/badge/postgres-0B96B2?style=for-the-badge&logo=postgresql&logoColor=white"/> 

- **Backend**: Django, Django Rest Framework
- **IDE**: VS Code
- **API Testing**: Postman
- **Version Control**: Git and GitHub
- **Database**: PostgreSQL

### Backend Setup Instructions

- Fork and Clone the repo using
```
$ git clone https://github.com/rudrakshi99/PizzaBackend.git
```
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/bin/activate
```
- Install dependencies using
```
$ pip3 install -r requirements.txt
```
- Make migrations using
```
$ python3 manage.py makemigrations
```
- Migrate Database
```
$ python3 manage.py migrate
```
- Create a superuser
```
$ python3 manage.py createsuperuser
```
- Run server using
```
$ python3 manage.py runserver
``` 

## Endpoints 
1. **Get Request:**
   
   ``end-point: /pizzas/``
   
   Accepted Response : status 200 OK
   
   Error Response : status 404 Not Found 
   
    ``end-point: /pizzas/id``
    
   Accepted Response : status 200 OK
   
   Error Response : status 404 Not Found 
   
2. **Post Request:**
   
   ``end-point: /pizzas/``
   
   Accepted Response : status 201 Created
   
   Error Response : {"error": "Invalid choice"} status 400 Bad Request
   
3. **Patch Request:**
   
   ``end-point: /pizzas/id``
   
   Accepted Response : status 200 OK
   
   Error Response : {"error": "Invalid choice"} status 400 Bad Request
   
4. **Delete Request:**
   
   ``end-point: /pizzas/id``
   
   Accepted Response : status 204 No Content 
   
   Error Response : status 404 Not Found 

5. **Filtration:**

   Add the valid choice number at the end of `=` in the end-point.
   
   ``end-point: /pizzas/?pizza_type=&pizza_size=&pizza_toppings=`
   
   Accepted Response : status 200 OK
   
   Error Response : status 400 Bad Request
   
   
# License :memo:

This project follows the [MIT License](https://choosealicense.com/licenses/mit/).
