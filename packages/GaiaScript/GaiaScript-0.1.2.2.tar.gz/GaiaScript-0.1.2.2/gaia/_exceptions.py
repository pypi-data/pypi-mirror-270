class TemplateNotFoundException(Exception):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} not found")


class DebugScriptNotFoundException(Exception):
    def __init__(self, debug_script_name):
        super().__init__(f"Debug script {debug_script_name} not found")


class TemplateAlreadyExistsException(Exception):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} already exists")


class ReplaceDictMustStartWithDollarSignException(Exception):
    def __init__(self, key):
        super().__init__(f"Replace dict must start with a dollar sign, {key}")


class DebugScriptAlreadyExistsException(Exception):
    def __init__(self, debug_script_name):
        super().__init__(f"Debug script {debug_script_name} already exists")
