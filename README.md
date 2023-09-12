# Handlelisten
A command-line interface shopping list created using Python

[Video Demo]("""""")

Description: This program is a shopping list which is able to add Norwegian procucts using [Kassalapp](https://kassal.app/api) API. The program has the ability to search and add products to the shopping list, view the shopping list, calculate the total price for the shopping list and remove products from the shopping list.

My first idea was to create something health/fitness related. I wanted to know which products had the most protein and was cheapest. Because of limitations in the API I decided to use the API for something else.

I am happy with the result, but found unit testing API results difficult. The function that searches and add products is therefore not unit tested.

---
## Functions

legge_til() is a function which does two things. It search for products and gives you the ability to add them to your shopping list. The function uses the Kassalapp API and gets a input from the user which becomes one of the paramters which the API uses to search. The function then converts the data to JSON and loops into it fetching the name, price and and store. After that 10 products get appended to a list which is displayed using tabulate so that the user can see the results. If the product the user is searching for is in the results the user can input the number of the product and append it to a global list. The function also has to sub-functions only used in this function for input validation called "ja_nei()" and "få_tall()". I found it difficult to test this function because it takes multiple user inputs and uses data from API which can change. I would likte to learn how to handle this in the future.

regnut_t(handleliste) is a simple functon which calculates the total price of the products in the shopping list. The function uses a variable to keep track of the total amount and a loop to access the dictionaries inside the shopping list and retrieve the value of "Price in NOK". After the loop ends in returns the total amount. If the list is empty the function returns a message letting the user know.

---

## Installation
Use [pip](https://pip.pypa.io/en/stable/) to install the package `tabulate` and `requests`
```
$ pip install tabulate
```

```
$ pip install requests
```

---

## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```

---
