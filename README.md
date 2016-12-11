Coding Test
====================

## Author

__Ahsanuzzaman Khan__

## Question 1

__What's your proudest achievement? It can be a personal project or something you've
worked on professionally. Just a short paragraph is fine, but I'd love to know why
you're proud of it, what impact it had (If any) and any insights you took from it.__

I'm extremely proud of my ongoing projects, where I have to build a social media website in Python/Django REST from scratch. I have good exprience with Django,
but had no idea about REST API where users will upload lots of photos and videos as well as do others things which are common any social media.

I developed Backend, Database and Testing / QA, and performance analysis. I have to handle lots of requests at a time so I decided to 
handle them asynchronously. I did necessary configuration with Python server (gunicorn) as well as postgresql (which can also handle requests asynchronously).
The website now can handle over 10K requests simultenously including videos, photos uploading.

This is an amazing learning experience, and taught me a lot about Python (wsgi) webservers (especially Gunicorn).


## Question 2

__Write a function that will flatten an array of arbitrarily nested arrays of integers
into a flat array of integers. e.g. [[1,2,[3]],4] → [1,2,3,4]. If the language you're
using has a function to flatten arrays, you should pretend it doesn't exist.__

You'll find the solution of this question in the `program-1` directory of the project. You
can run the tests to make sure it works:

```bash
$ python3 flatten_array.py
```

or you can run the test as well:

```
python3 -m unittest tests_flatten_array.py
```


## Question 3

__We have some customer records in a text file (customers.json) -- one customer per
line, JSON-encoded. We want to invite any customer within 100km of our Dublin office
for some food and drinks on us. Write a program that will read the full list of
customers and output the names and user ids of matching customers (within 100km),
sorted by User ID (ascending).__

The solution lives in the `program-2` directory. You can see the results by executing the
script:

```bash
$ python3 invite_customers.py

# Optionally, you can run the tests as well:
$ python3 -m unittest tests_invite_customers.py
```

