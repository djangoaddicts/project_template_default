# project_template_default
A reusable template for making django projects

<br/>

## suggested use
1. create a new repo using the DjangoAddicts repo template: https://github.com/djangoaddicts/repo_template 

2. create a new python virtual environment:

    ```python -m venv venv```

3. install the packages defined in the toml file:

    ```pip install .[dev]```

4. use the following command to create a django project based on the django project template:

    ```django-admin startproject my_project_name --template https://github.com/djangoaddicts/project_template_default/archive/refs/heads/main.zip```

5. rename the project name to "django_project":
    
    ```mv <my_project_name> django_project```

6. cd into django_project and use the following command to create a django app based on the django app template:

    ```./manage.py startapp my_app --template https://github.com/djangoaddicts/app_template_default/archive/refs/heads/main.zip --extension htm```

7. cd to the django_project directory, run migrations, create an admin user, and start the demo server:

    ```
    cd django_project
    ./manage.py migrate 
    ./manage.py add_superuser
    ./manage.py runserver 
    ```

8. open a browser at 127.0.0.1:8000, log in with admin/admin
