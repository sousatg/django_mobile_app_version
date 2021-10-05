# Django Mobile App Version

## Quick start

1. Install the lob
```
pip install django-mobile-app-version
```

2. Add `mobile_app_version` to your *INSTALLED_APPS* settings like:
```
INSTALLED_APPS = [
    mobile_app_version
]
```

3. Include the Mobile App Version URLconf in your projects `urls.py` like this:
```
path('', include('mobile_app_version')),
```

4. Run `python manage.py migrate` to create the models.

5. Start the development server and visit http://127.0.0.1:8000/admin/ to create a app version (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/app-versions/ 
