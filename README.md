# bluvector

This is an web application that allows visitors add, rate and leave reviews for beers
## Set Up Running
- Download & unpack .zip file
- Assuming you already have python and pip, install requirements using `​ pip install -r requirements.txt` within command prompt or terminal
- Run the command `python manage.py runserver`
- On your browser, go to http://127.0.0.1:8000/ or whatever server address was provided in terminal

## Requirements
- [x] Use a Python framework of your choice for the server side processing
- [x] Use a persistent database of your choice to store the data
- [x] Use a front-end design/layout framework of your choice to provide the base styling and
structure for the application
- [x] Utilize AJAX to populate the data on the landing

## Expectations
### View Product 
 Upon visiting the site, you shall be presented a view of the highest rated items, as well as a view of the most recently rated/reviewed items. 
### View Product Details     
Navigating to a beer returns a detailed view of it (i.e. beer name, brewery, style, ABV, description & overall rating) as well as and any reviews (rating, username of reviewer, time of comment & comments left)that have been written for it.
- Each product shows a maximum of 4 reviews at once but allows you scroll with footer navigation
    
 ### Leave Review
 When viewing a beer, you have an option leave a review for that beer. When reviewing, you would provide a 1 to 5 rating for the beer as well as an optional comment section below. (Click to Submit).
 - Click "Leave Review" button to show review forms, you can submit or close forms.
 - The page automatically shows your recently left review
 - You can go back to view all Beers & ratings

### Add Product
While viewing highest rated or recently reviewed items, you can add new items for rating and review. When adding new beers, you would be prompted to fill out details about the beer and then to submit or close form.
- Click "Add Product" button to show review forms, you can submit or close forms.
- A brewery is selected from list of Breweries featured on the app
- Breweries are chosen and added to database my admin
- After adding product, you shall be taken to product page to leave review.

