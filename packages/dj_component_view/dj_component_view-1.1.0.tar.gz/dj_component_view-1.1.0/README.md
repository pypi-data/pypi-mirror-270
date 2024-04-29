# dj_component_view

This project lets you create reusable Django views from [jinjax](https://jinjax.scaletti.dev/) templates

## Usage

```python
from dj_component_view import ComponentView
from djecorator import Route

route = Route()

@route("/greet")
class GreetView(ComponentView):
    component = "Greeting"

    def context(self, request):
        return {
            "name": request.GET.get("name", "World"),
        }
```
