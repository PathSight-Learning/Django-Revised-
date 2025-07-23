# Django Career Path Application

This Django application provides a comprehensive career path exploration system for various technology fields including Software Development, Data Science, Cybersecurity, and Research.

## Project Structure

```
Django-Revised--master/
├── careerpath/           # Main app directory
│   ├── models.py         # Database models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── load_data.py      # Data loading script
│   ├── templates/        # HTML templates
│   └── migrations/       # Database migrations
├── djangophase1/         # Django project settings
│   ├── settings.py       # Project configuration
│   └── urls.py           # Main URL routing
└── manage.py             # Django management script
```

## Issues Encountered and Fixes Applied

### 1. Module Import Issues

**Problem**: `ModuleNotFoundError: No module named 'django'`
- **Root Cause**: The script was being run outside of the virtual environment where Django is installed. When you run a Python script directly, it uses the system Python environment, not your project's virtual environment.
- **Technical Details**: Virtual environments isolate Python packages per project. Django was installed in `myvenvc/` but the script was running in the system Python environment.
- **Solution**: Activate virtual environment before running scripts
```bash
source myvenvc/bin/activate
```

**Problem**: `ModuleNotFoundError: No module named 'djangophase1'`
- **Root Cause**: Python couldn't find the Django project module because the project root directory wasn't in the Python path. When running a script directly, Python only adds the script's directory to `sys.path`, not the project root.
- **Technical Details**: Django needs to find the `djangophase1` module to load settings, but Python's import system couldn't locate it from the script's context.
- **Solution**: Added project root to Python path in the script
```python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```
This ensures that when Django tries to import `djangophase1.settings`, Python can find the module.

### 2. Relative Import Issues

**Problem**: `ImportError: attempted relative import with no known parent package`
- **Root Cause**: Using relative imports (`from .models import ...`) in a script that's being run directly. Relative imports only work when a module is imported as part of a package, not when executed as a standalone script.
- **Technical Details**: When you run `python3 careerpath/load_data.py`, Python treats it as the `__main__` module, not as part of the `careerpath` package. Therefore, the relative import `.models` has no parent package context.
- **Solution**: Changed to absolute imports
```python
# Before:
from .models import Field, Subfield, Skill, JobExample, LearningResource, RealWorldProject

# After:
from careerpath.models import Field, Subfield, Skill, JobExample, LearningResource, RealWorldProject
```
This tells Python to look for the `careerpath` package in the Python path and import `models` from it.

### 3. Database Model Issues

**Problem**: `IntegrityError: NOT NULL constraint failed: careerpath_subfield.field_id`
- **Root Cause**: The `Subfield` model has a ForeignKey to `Field` that is defined as `NOT NULL` (required), but the script was trying to create `Subfield` objects without specifying which `Field` they belong to.
- **Technical Details**: Django's ORM enforces database constraints. The `Subfield` table has a `field_id` column that cannot be NULL, but the script was only providing a `name` when creating subfields.
- **Solution**: Updated Subfield creation to include the field parameter
```python
# Before:
subfield, _ = Subfield.objects.get_or_create(name=subfield_data['name'])

# After:
subfield, _ = Subfield.objects.get_or_create(name=subfield_data['name'], field=field)
```
This ensures each `Subfield` is properly linked to its parent `Field` as required by the database schema.

**Problem**: `TypeError: JobExample() got unexpected keyword arguments: 'career_path'`
- **Root Cause**: The script was trying to create `JobExample` objects with a `career_path` parameter, but the model didn't have a field with that name. The model only had `field`, `title`, `description`, and `key_skills` fields.
- **Technical Details**: Django's model creation validates all keyword arguments against the model's field definitions. Any unexpected arguments raise a TypeError.
- **Solution**: Added ForeignKey to Subfield in JobExample model
```python
class JobExample(models.Model):
    field = models.ForeignKey(Field, related_name='jobs', on_delete=models.CASCADE)
    subfield = models.ForeignKey(Subfield, related_name='job_examples', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    key_skills = models.ManyToManyField(Skill, related_name='job_examples')
```
This allows jobs to be linked to specific subfields, providing more granular categorization.

### 4. Migration Issues

**Problem**: Django required a default value for new non-nullable field
- **Root Cause**: When adding a new required field to an existing model that already has data, Django needs to know what value to assign to existing rows for the new column.
- **Technical Details**: SQL databases require all columns to have values. When you add a NOT NULL column to a table with existing data, the database needs a default value to populate existing rows.
- **Solution**: Made field nullable initially, then migrated
```python
subfield = models.ForeignKey(Subfield, related_name='job_examples', on_delete=models.CASCADE, null=True, blank=True)
```
This allows the migration to succeed with existing data, and you can later populate the field and make it non-nullable if desired.

### 5. Field Name Mismatch

**Problem**: `AttributeError: 'JobExample' object has no attribute 'skills'`
- **Root Cause**: The script was trying to access a `skills` attribute on `JobExample` objects, but the model defines the many-to-many relationship as `key_skills`, not `skills`.
- **Technical Details**: Django creates attribute names based on the field names in your model. The model had `key_skills = models.ManyToManyField(...)`, so the attribute is `key_skills`, not `skills`.
- **Solution**: Updated to use correct field name
```python
# Before:
job.skills.add(skill)

# After:
job.key_skills.add(skill)
```
This matches the actual field name defined in the model.

### 6. URL Namespace Issues

**Problem**: `NoReverseMatch: 'careerpath' is not a registered namespace`
- **Root Cause**: The templates were using URL namespace syntax (`{% url 'careerpath:view_name' %}`), but the main URL configuration didn't register the `careerpath` namespace.
- **Technical Details**: Django's URL system uses namespaces to organize URLs from different apps. When you use `careerpath:view_name` in templates, Django looks for a namespace called `careerpath` in the URL configuration.
- **Solution**: Added namespace to URL configuration
```python
# Before:
path('', include('careerpath.urls')),

# After:
path('', include(('careerpath.urls', 'careerpath'), namespace='careerpath')),
```
This tells Django that URLs from `careerpath.urls` should be accessible under the `careerpath` namespace.

## How to Run the Application

1. **Activate Virtual Environment**:
   ```bash
   source myvenvc/bin/activate
   ```

2. **Run Migrations**:
   ```bash
   python3 manage.py migrate
   ```

3. **Load Data** (if needed):
   ```bash
   python3 careerpath/load_data.py
   ```

4. **Start Development Server**:
   ```bash
   python3 manage.py runserver
   ```

## Data Loading Script

The `load_data.py` script populates the database with career path information including:
- **Fields**: Main career categories (Software Development, Data Science, etc.)
- **Subfields**: Specific areas within each field
- **Job Examples**: Detailed job descriptions with requirements
- **Skills**: Technical and soft skills for each job
- **Learning Resources**: Links to educational materials
- **Real-World Projects**: Project ideas for portfolio building

## Models Overview

- **Field**: Main career categories
- **Subfield**: Specific areas within fields
- **Skill**: Technical and soft skills
- **JobExample**: Detailed job descriptions with requirements
- **LearningResource**: Educational resources and links
- **RealWorldProject**: Project ideas for practical experience

## Key Lessons Learned

1. **Always activate virtual environment** before running Django commands
2. **Use absolute imports** in standalone scripts, not relative imports
3. **Check model relationships** carefully when creating objects
4. **Make new fields nullable** initially when adding to existing models
5. **Verify field names** match exactly between models and code
6. **Configure URL namespaces** when templates use namespace syntax
7. **Test incrementally** to catch issues early in the development process

## Troubleshooting

If you encounter similar issues:

1. Check virtual environment activation
2. Verify import statements (absolute vs relative)
3. Review model relationships and field names
4. Ensure migrations are applied
5. Check URL configuration for namespaces
6. Validate template syntax and URL references

## Common Django Development Patterns

### Running Standalone Scripts
When creating scripts that need to interact with Django models:
```python
import os
import django
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')
django.setup()

# Now you can import and use Django models
from yourapp.models import YourModel
```

### Adding Fields to Existing Models
When adding required fields to models with existing data:
1. Make the field nullable initially (`null=True, blank=True`)
2. Create and run migrations
3. Populate the field with data
4. Make the field non-nullable if needed
5. Create another migration

### URL Namespace Configuration
When using namespaced URLs in templates:
```python
# In main urls.py
path('app/', include(('app.urls', 'app'), namespace='app'))

# In templates
{% url 'app:view_name' %}
``` 