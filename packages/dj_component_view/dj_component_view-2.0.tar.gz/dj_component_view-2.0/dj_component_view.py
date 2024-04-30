from importlib import import_module

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views import View


class ComponentView(View):
    component = None
    method = None

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

    def dispatch(self, request, *args, **kwargs):
        if self.method is not None and request.method.lower() != self.method.lower():
            return HttpResponseNotAllowed([self.method])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.method is None or self.method.lower() == "get":
            context = self.context(request)
            return self.render_to_response(context)
        return HttpResponseNotAllowed(["GET"])

    def post(self, request, *args, **kwargs):
        if self.method is None or self.method.lower() == "post":
            context = self.context(request)
            return self.render_to_response(context)
        return HttpResponseNotAllowed(["POST"])

    def context(self, request):
        return {}
