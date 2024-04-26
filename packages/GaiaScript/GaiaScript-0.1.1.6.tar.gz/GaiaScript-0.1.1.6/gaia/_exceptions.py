class TemplateNotFoundException(Exception):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} not found")


class TemplateAlreadyExistsException(Exception):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} already exists")
