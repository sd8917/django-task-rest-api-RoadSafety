# Django-Task-road-safety
A task given by roadSafety campaign

## About the project
* This is simple e-commerce website which is populated with some data and we are going make a rest_api for retrival,update and delete
using django restframework a library provide by Django.

#### How to setup on local machine i.e requirements needed to run the project
```
python 3
pip install requirements.text
```
simple it will setup all required package on your local machine.

## What the project do
* show all product view :GET
* Show detail for a product view : GET/products/{id}/
* Shopping cart view : GET/cart .

## We user concept of serialization.

### To test in console all product view :GET 
* This will give you the list of the all product on the endpoint   http://127.0.0.1:8000/api/v1/products/ 
```
>>> from store.models import Product
>>> product = Product.objects.all()[0]

>>> from store.serializers import ProductSerializer

>>> serializer = ProductSerializer()

>>> data = serializer.to_representation(product)

>>> from rest_framework.renderers import JSONRenderer

>>> renderer = JSONRenderer()

>>> renderer.render(data)

```
![Screenshot (168)](https://user-images.githubusercontent.com/34008023/84311628-3d8cf400-ab81-11ea-9a92-de7391bd6462.png)


## Next
* we have added the feature if the number of product more than the 3 for pagination using rest_framework package and filter the product according to the id or name.Let's a look by visiting this endpoint   http://127.0.0.1:8000/api/v1/products/
* Then , go to filter and submit with any id let's 1.
* Have a look how it looks in the browser

![Screenshot (170)](https://user-images.githubusercontent.com/34008023/84312129-14209800-ab82-11ea-8de8-292c72a1522a.png)


## Next
* A endpoint to create a product http://127.0.0.1:8000/api/v1/products/new
* It looks in browser 

![Screenshot (172)](https://user-images.githubusercontent.com/34008023/84312571-c8222300-ab82-11ea-957e-fe067a78d936.png)



## Next
* A endpoint to update and delete a product from table http://127.0.0.1:8000/api/v1/products/1/
here 1 is product id for updatating or deleting.

* let's have a look at this end point

![Screenshot (174)](https://user-images.githubusercontent.com/34008023/84316843-77fa8f00-ab89-11ea-89ce-576bbbd8f4a0.png)





        
