# Products app
Application simulating a part of the online shop software. The app stores information about the products and their categories.
Each of the product can link to many categories and each category can link to many products. Categories are defined by the user, hence are stored in the database.
Templates used in the project extend the base template.

Views:
- list of categories in alpfabetical order
- lists all products
- contains the add, modify product and category

The views in the app are restricted for logged in users, with permissions. Created with class based views. Models are registered in django-admin.
