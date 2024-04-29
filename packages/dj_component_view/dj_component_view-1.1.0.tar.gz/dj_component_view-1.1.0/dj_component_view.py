from importlib import import_module

from django.http import HttpResponse
from django.views import View
from django.conf import settings


class ComponentView(View):
    component = None

    def get_catalog(self):
        for template_engine in settings.TEMPLATES:
            if template_engine["BACKEND"] == "django.template.backends.jinja2.Jinja2":
                env_string = template_engine["OPTIONS"]["environment"]
                module_path, function_name = env_string.rsplit(".", 1)
                module = import_module(module_path)
                environment_function = getattr(module, function_name)
                return environment_function().globals["catalog"]
        raise ValueError("Jinja2 template engine not found in settings.")

    def render_to_response(self, context):
        catalog = self.get_catalog()
        if not self.component:
            raise ValueError("ComponentView subclasses must define a component.")
        return HttpResponse(str(catalog.render(self.component, **context)))

    def get(self, request, *args, **kwargs):
        context = self.context(request)
        return self.render_to_response(context)

    def context(self, request):
        return {}
