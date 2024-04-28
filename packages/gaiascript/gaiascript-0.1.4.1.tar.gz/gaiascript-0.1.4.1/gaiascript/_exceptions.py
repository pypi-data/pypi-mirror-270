class GaiaException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class TemplateNotFoundException(GaiaException):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} not found")


class DebugScriptNotFoundException(GaiaException):
    def __init__(self, debug_script_name):
        super().__init__(f"Debug script {debug_script_name} not found")


class TemplateAlreadyExistsException(GaiaException):
    def __init__(self, template_name):
        super().__init__(f"Template {template_name} already exists")


class ReplaceDictMustStartWithDollarSignException(GaiaException):
    def __init__(self, key):
        super().__init__(f"Replace dict must start with a dollar sign, {key}")


class DebugScriptAlreadyExistsException(GaiaException):
    def __init__(self, debug_script_name):
        super().__init__(f"Debug script {debug_script_name} already exists")
