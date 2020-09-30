# YouFetch

### Installing depencies:---

- Django3.0.6  - to install django, type below command in linux terminal

  - ```bash
    pip3 install Django
    ```

- Django-rest-framework - to install it, type the below command in linux terminal

  - ```bash
    pip3 install djangorestframework
    ```

- Django background Task : Type the below command to install it on linux

  - ```
    pip3 install django-background-tasks
    ```

### Run the server:---

- first go inside the root directory of the project named "tubeFetch" and run these two commands in two separate terminals

  - ```
    Python3 manage.py makemigrations
    ```

  - ```
    python3 manage.py migrate
    ```

  - ```bash
    python3 manage.py runserver
    ```

  - ```
    python3 manage.py process_tasks
    ```

### About UI:---

- ​	go to the below link in a browser

  - ```
    http://localhost:8000/search/
    ```

- There, you will see a navbar where there links are present, 
  - [home](http://localhost:8000/search/)
    - Home is the landing page
  - [See data in UI](http://localhost:8000/search/get-data/)
    - After clicking on this link, you will see a list of youtube videos which are already fetched and saved in our database in UI. Pagination is also there and the data will be in the reverse chronological order sorted by date.
  - [See Data in API format](http://localhost:8000/search/get-videos/1)
    - After clicking on this link, you will see a list of youtube videos which are already fetched and saved in our database as an API response. the data will be in the reverse chronological order sorted by date. to paginate, you can pass different number in the url parameter, like 1,2,3,4,5,.... and you will get the paginated data

Here the query is "cricket" and I have given my own API_KEY of google account so that you can test it easily.