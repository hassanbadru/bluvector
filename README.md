# bluvector

This is an web application that allows visitors add, rate and leave reviews for beers
## Set Up Running
- Download & unpack .zip file
- Assuming you already have python and pip, install requirements using `​ pip install -r requirements.txt` within command prompt or terminal
- Run the command `python manage.py runserver"
- On your browser, go to http://127.0.0.1:8000/ or whatever server address was provided 

## Requirements
- [x] Use a Python framework of your choice for the server side processing
- [x] Use a persistent database of your choice to store the data
- [x] Use a front-end design/layout framework of your choice to provide the base styling and
structure for the application
- [x] Utilize AJAX to populate the data on the landing

## Expectations
### Product View
    Upon visiting the site, you shall be presented a view of the highest rated items, as well as a
    feed of the most recently rated/reviewed items. 
### Product Details View    
    Navigating to a beer returns a detailed view of it (i.e. beer name,
    brewery style & overall rating) as well as and any reviews (rating, username of reviewer, time of comment & comments left)that have been written for it.
    - Each product shows a maximum of 4 reviews at once but allows user scroll with footer navigation
    
 ### Reviews View
    When reviewing, the user shall be required to provide a 1 to 5 rating of a specific instance of
    the product or service you choose to build your application for. There shall also be an optional
    comment field to provide a written review.

### Add Product
This service shall also allow for users to add new items for rating and review. When creating
new items, the user must fill out what ever meta-data you’ve deemed relevant to collect about
the product or service under review.
