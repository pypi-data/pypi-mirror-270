# dj_component_view

This project lets you create reusable Django views from [jinjax](https://jinjax.scaletti.dev/) templates.

## Usage

### Greeting.jinja

```jinja
{#def name #}

<h1>hello, {{ name }}</h1>
```

### views.py

```python
from dj_component_view import ComponentView
from djecorator import Route

route = Route()

@route("/greet")
class GreetView(ComponentView):
    component = "Greeting"

    def context(self, request):
        return {
            # by default, the view expects a POST request
            "name": request.POST.get("name", "World"),
        }
```

### index.html with [htmx](https://htmx.org)

```html
<form hx-post="/greet" hx-trigger="submit">
  <input type="text" name="name" placeholder="Enter your name" />
  <button type="submit">Greet</button>
</form>
```

### Specifying the Allowed HTTP Method

You can set the method class variable in your ComponentView subclass to specify the allowed HTTP method for the view. The default value is None, which means both GET and POST methods are allowed.

- If `method` is set to `"GET"`, only GET requests will be allowed.
- If `method` is set to `"POST"`, only POST requests will be allowed.

If the incoming request's method does not match the specified method, a 405 Method Not Allowed response will be returned.

### Overriding the get and post Methods

If you need more control over the handling of GET and POST requests, you can override the get and post methods in your ComponentView subclass.

```python
@route("/custom")
class CustomView(ComponentView):
    component = "CustomComponent"
    method = "get"

    def get(self, request, *args, **kwargs):
        # Custom implementation of the GET method
        ...
```
