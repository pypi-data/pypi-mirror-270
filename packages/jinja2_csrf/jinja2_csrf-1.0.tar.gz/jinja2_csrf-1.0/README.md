# Jinja2 CSRF Token Extension

This is a Jinja2 extension for generating CSRF tokens in Django templates.

## Installation

Install the extension using pip:

```bash
pip install jinja2_csrf
```

## Configuration

To use this extension, you need to configure Jinja2 as a template engine in your Django settings:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'path.to.your.jinja2.environment',
            'extensions': ['jinja2_csrf.CSRFTokenExtension'],
        },
    },
]
```

Make sure to replace 'path.to.your.jinja2.environment' with the actual path to your Jinja2 environment.

## Usage

In your Jinja2 templates, you can now use the csrf_token tag to generate a CSRF token:

```html
<form method="post">
    {% csrf_token %}
    <!-- Your form fields go here -->
    <button type="submit">Submit</button>
</form>
```

The csrf_token tag will generate an `<input>` element with the CSRF token value:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
```

Make sure to include the csrf_token tag within your form to protect against CSRF attacks.
