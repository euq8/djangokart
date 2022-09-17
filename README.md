## Setup Project
1. pip install -r requirement.txt
2. django-admin startproject djangokart . # to create django project in current dir.
3. python3 manage.py runserver > go to 127.0.0.1:8000
4. Add urlpatterns in djangokart/urls.py
5. Add views.py and implement different views inside it.
6. Add templates folder and add home.html file and put simple html.
7. Add static folder and css and images in it.
8. Add some settings in setting.py
9. Run python3 manage.py collectstatic

## Django Custom User Model, Category and Media Files
1. Create Apps (Category, Product, Order, Store etc.)
    ### Category Model
    1. create `category` app >> python3 manage.py startapp category
