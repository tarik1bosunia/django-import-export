### install [django-import-export](https://django-import-export.readthedocs.io/en/latest/installation.html) package

```shell
 pip install django-import-export
```

#### settings.py
```python
INSTALLED_APPS = (
    ...
    'import_export',
)
```

### admin.py
```python
from django.contrib import admin

from employee.models import Employee

from import_export.admin import ImportExportModelAdmin

admin.site.register(Employee, ImportExportModelAdmin)
```