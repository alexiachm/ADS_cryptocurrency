# ADS_cryptocurrency
Cyptocurrency Project for Advanced Data Structures and Storage

# HTML code description
The code should be a html and it starts with the usual structure tags: <!DOCTYPE html>, <html>, <head>, and <body>.

Inside the <head> section, there are <meta> tags for defining the character set and, a <title> tag for setting the page title, and a <style> section for inserting CSS styles into the document (computer language for laying out and structuring web pages).
The CSS styles define the appearance of various elements on the page.
Styles are set for the body, header, input fields, buttons, containers, list items, links, etc.
Header Section: It contains a form for user input, in this case for searching cryptocurrencies.
Input field for entering a search query and a submit button.
Results Section: This section is conditionally rendered ({% if currency %}) and contains the search results.
It displays information about each cryptocurrency returned from the search.
Information includes the name, NIF, founder, date founded, consensus mechanism, max supply, circulating supply, total supply, market cap, website link, whitepaper link, GitHub link, Reddit link, and possibly other fields.
Results are displayed in an unordered list (<ul>) with list items (<li>).
Title Container: It contains an image (<img>) and a title (<h1>).
The image is a visual representation related to cryptocurrency that was uploaded to pythonanywhere. 
The title is “Search cryptocurrencies”
Message Section: In this section the code would display content based on whether there is a message to show or not.
Variables: This HTML template seems to be using a templating engine (e.g., Jinja2) as it includes variables like {{ currency_data.name }}, {{ currency_data.NIF }}, etc.
These variables are placeholders for dynamic content that will be filled in by the backend server when the page is rendered.

# FLASK code description
Line by line, first the necessary modules from Flask are imported, as well as the TinyDB and the Query classes from TinyDB. Then, we create a flask application instance, a TInyDB database instance with the JSON file named ‘crytpo_info_db.json’, and a table named ‘crypto-info’ within the TinyDB database to store cryptocurrency information. With the @app.route('/', methods=['GET', 'POST']), we define a route for the rool URL that accepts both the GET and POST requests. After this, we created a function named ‘index()’ where inside we could check if the incoming request method is POST, and retrieve the value of the ‘search_input’ from the form submitted with leading and trailing spaces, check if the ‘search_input’ is not empty, and lastly create a query object for the TinyDB database. Outside the function, we search the ‘crypto_info table for records where the ‘NIF’ or ‘name’ matches the ‘search_input’. Then check if any records were found in the database matching the search criteria, and render the ‘index.html’ with the found cryptocurrency information passed to it. After that you render the ‘index-html’ with a message indicating no results were found for the provided search input, and also render the template with a message indicating that the user should enter a symbol or NIF. Lastly check if the script is being run directly and start the Flask application in debug mode if the script is being run directly. 



# TINYDB code description 
We made the following code in order to create a Jason file, using TinyDB, to hold the data from the cryptocurrencies we have researched. As mentioned before, we use a No SQL database for this project as we do not have the same information for all cryptocurrencies. We begin the code by creating a TinyDB table called “crypto_info_db” in which we will store our data. Next we create a dictionary with the cryptocurrency code as keys, and all the information we gathered for each one as the values. Then we use the “insert_multiple” command to add all the data from our dictionary into the TinyDB table, which will allow us to transfer the data into the Jason file. With this file created we can proceed with the following steps for our website.
