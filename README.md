## Project Dependencies

* Python --version 3.6+
* pip


## To Setup the Project follow these step:

* git clone [repo]
* cd [repo]
* sudo apt-get install python-virtualenv
* sudo apt install python3-pip
* python3 -m venv env
* source env/bin/activate
* pip install -r requirements.txt



## Api

#### Get Auth Token
 * localhost:8000/api-token-auth/email=test password=123
 
 #### Login User
 * localhost:8000/api/users/ -H 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'

#### Add Ingredients

* localhost:8000/api/products/ingredients/add/

data = {
    'name':'egg'
}

#### Add products

* localhost:8000/api/products/add/

data =  {
    "name":"',
    "ingredients": [1,2],
    "ingredients_details':{
        'ingredients':[
        {'name':'egg', 'quantity':'50%'},{'name':'milk', 'quantity':'50%'}
        ]
    },
    "cost_price":50,
    "selling_price":100,
    "discount":0

}


#### Place order

* * localhost:8000/api/users/orders/create/

data = {
    'products':[1,2],
    'products_details':
    {
        'products':[{
            'id':1,
            'name':'cake',
            'quantity':3
        }]
    }
    
}

Output  =  {
    'user':1,
    'products':[1,2],
    'products_details':{
        'products':[{
            'id':1,
            'name':'cake',
            'quantity':3
        }]
    },
    'total_price':300

}