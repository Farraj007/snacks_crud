# **Lab: Django CRUD and Forms**

## **Feature Tasks and Requirements**

- Create snacks_crud_project Django project

- Create snacks app

- Create Snack model
    - title field
    - purchaser field
    - description field
    - Register model in admin
    
<br>

### **Views for Snacks App**


- Create SnackListView
    - extends ListView
    - give a template of snack_list.html
    - associated url path is an empty string

<br>

- Create SnackDetailView
    - extends DetailView
    - give a template of snack_detail.html
    - associated url path is ```<int:pk>/```

<br>

- Create SnackCreateView
    - extends CreateView
    - give a template of snack_Create.html
    - associated url path is ```Create/```

<br>

- Create SnackUpdateView
    - extends UpdateView
    - give a template of snack_update.html
    - associated url path is ```<int:pk>/update/```

<br>

- Create SnackDeleteView
    - extends DeleteView
    - give a template of snack_delete.html
    - associated url path is ```<int:pk>/delete/```

<br>

- Add urls to support all views, with appropriate names

- Add templates to support all views

- Add navigation links in appropriate locations to access all pages



<br>

### ***Templates***

In this Lab, I used Bootstrap to create the templates. Specifically, the "Personal Template"


1. So I did the following:

    In the settings file, make the following changes:

    ```
    STATIC_URL = 'static/'

    STATIC_ROOT = BASE_DIR / 'static'

    Run manage.py collectstatic
    ```

    This command will creates a **static folder** that has static files for the built-in app (admin) but not our own app, and in this case I should do the following:
1. go inside my app
2. make a folder with the name “**static**” with another folder inside of it “**snacks**”
then copy paste from the bootstrap assets into the snacks/static/snacks
3. then run 
```python manage.py collectstatic``` ,,, to take the new static files for our app
4. Make templates and make sure to use the Django Template Lanaguage
5. Use {% load static %} in the _base.html  template.
6. Create the rest of the templates and add the appropriate navigation links.
