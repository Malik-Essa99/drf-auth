## lab 33
### project: Authentication & Production Server Overview
### Author: Malik Al Hudrub
### How to initialize/run your application:

+ clone 
+ pip install -r requirements.txt
+ open docker on windows
+ on VsCode terminal: docker-compose up
 

### For testing manually using thunder client


##### API Tokens:

Access Token:

method: Post

url: http://127.0.0.1:8000/api/token/
bearer:

```
    {
        "username": "admin",
        "password": "123",
        "owner": 1
    }

```

Refresh Token:

method: Post

url: http://127.0.0.1:8000/api/token/refresh/

body:

```
    {
        {
        "refresh": "Your refresh token"
        }
    }

```




##### Api CRUD routes:

```
    route: http://127.0.0.1:8000/api/v1/movies/

```

