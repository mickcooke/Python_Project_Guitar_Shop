"Guitaarrr Shop Inventory," an app by Mick Cooke, June 2023.
Created using Python.

WELCOME

Welcome to my Python project, made as part of the 16 week CodeClan Software Development bootcamp. I have made a shop inventory for an imaginary guitar shop, the pirate-themed 'guitaarrr!'.


RUNNING INSTRUCTIONS

You will need both psycopg2 and Flask installed to run this app. 

Download all files.
In Terminal, navigate into the folder python_project

Then type into Terminal:

dropdb guitar_manager

createdb guitar_manager

psql -d guitar_manager -f db/guitar_manager.sql

psql -d guitar_manager -f db/guitar_manager.sql

python3 console.py

flask run

Then command click the URL that appears in Terminal

Control C to exit Flask

--------------------------------------
THE BRIEF

The brief was to set up an inventory for a shop. I chose to set up a guitar shop inventory. 

MVP

The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.

The inventory should track manufacturers, including a name and any other appropriate details.

The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.

This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.

Show an inventory page, listing all the details for all the products in stock in a single view.

As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Possible Extensions

Calculate the markup on items in the store, and display it in the inventory
Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.

Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.

I got around to all extensions except for the last one- categorise your items.

TECHNOLOGIES USED

This project was written using Python, pSQL, HTML, CSS and Jinja. 



