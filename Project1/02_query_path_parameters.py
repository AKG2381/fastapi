
from enum import Enum
from typing import Optional
from fastapi import FastAPI,Query,Path
from pydantic import BaseModel

app = FastAPI()

@app.get('/',description='This is our first rout')
async def root():
    return {'message' : "Hello world"}


@app.post('/')
async def post():
    return {'message' : "Hello from post route"}


@app.put('/')
async def put():
    return {'message' : "Hello from put route"}


@app.get('/users')
async def list_users():
    return {'message' : "list users route"}

# put specific endpoint before dynamic endpoint
@app.get('/users/me')
async def get_current_user():
    return {'message' : "This is the current user"}


@app.get('/users/{user_id}')
async def get_users(user_id : str):
    return {'user_id' : user_id}

class FoodEnum(str ,Enum ):
    fruits = 'fruits'
    vegetables = 'vegetables'
    dairy = 'dairy'


# path parameters
@app.get('/foods/{food_name}')
async def get_food(food_name : FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {'food_name': food_name,
                'message' : 'You are Healthy'}
    if food_name == FoodEnum.fruits:
        return {'food_name': food_name,
            'message' : 'You are still Healthy but like sweet things'}
    return {'food_name': food_name,
        'message' : 'I like chocolate milk'}





# query and path parameters
fake_item_db = [{'item_name' : 'Foo'},{'item_name' : 'Bar'},{'item_name' : 'Baz'}]
@app.get('/items')
async def list_items(skip : int  =0, limit : int =10):
    return fake_item_db[skip : skip+limit]

@app.get('/items/{item_id}')
async def get_items(item_id : str, required_query_parameter : str,
                    q : str | None = None, short : bool = False):
    item = {'item_id' : item_id, 'required_query_parameter' : required_query_parameter}
    if q:
        item.update({'q' : q})
    if not short:
        item.update({'description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur viverra.'})
    return item


@app.get('/users/{user_id}/items/{item_id}')
async def get_user_items(user_id :int,item_id : str,q: str | None = None, short : bool = False):
    item =  {'item_id' : item_id, 'owner_id' : user_id}
    if q:
        item.update({'q' : q})
    if not short:
        item.update({'description' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur viverra.'})
    return item


class Item(BaseModel):
    name : str
    description : Optional[str] = None # python 3.6+
    price : float
    tax : float | None = None # python3.10+

# request Body

@app.post('/items')
async def create_items(item : Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax' : price_with_tax})
    return item_dict




@app.put('/items/{item_id}')
async def create_items_with_put(item_id : int,item : Item, q : str | None = None):
    result =  {'item_id' : item_id, **item.model_dump()}
    if q:
        result.update({'q' : q})
    return result


#   /item?q=ajeet&s=a&s=b&s=c
# {"items":[{"item_id":"Foo"},{"item_id":"Bar"},{"item_id":"Baz"}],"q":"ajeet","s":["a","b","c"]}
@app.get('/item')
async def read_items(q : str | None = Query(...,# this means this is required value does not have an~y default value
                                            # default='firstquery',
                                             min_length=3,
                                             max_length=10,
                                            #  regex='^firstquery$'
                                             ),
                    s : list[str] | None = Query(...,min_length=3,max_length=10),
                    t : str | None = Query(None,min_length=3,
                                           max_length=10,
                                           title='Sample query string',
                                           description='This is a sample query string',
                                           alias='item-query'
                                           )            
                    ):
    result = {'items' : [{'item_id' : 'Foo'},{'item_id' : 'Bar'},{'item_id' : 'Baz'}]}
    if q:
        result.update({'q' : q})
    if s:
        result.update({'s' :s})
    if t:
        result.update({'t' :t})
    return result



# this will work 
# http://127.0.0.1:8000/item/hidden?hidden_querry=foobar
# but won't show anything in swagger UI
@app.get('/item_hidden')
async def hidden_querry_route(hidden_querry : str | None = Query(None,
                                                        include_in_schema=False      

)):
    if hidden_querry:
        return {'hidden_querry' : hidden_querry}
    return {'hidden_querry' : 'Not Found'}


@app.get('/items_validation/{item_id}')
async def read_items_validation(*  # this astrics allows to put q after item_id,
                                #  this means all of the values after * are kwargs
                               , item_id : int = Path(...,title ='Id of the item to get',gt =10, le=100),
                                q : str ,
                                size : float = Query(...,gt=0,lt=7.75)
                                ):
    results = {'item_id' : item_id,'size': size}
    if q:
        results.update({'q' : q})
    return results

