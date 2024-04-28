import os.path

from ._exceptions import DebugScriptNotFoundException, \
    DebugScriptAlreadyExistsException


class DebugScriptManager:

    @staticmethod
    def check_debug_script_exists(func):
        def wrapper(self, *args, **kwargs):
            if not self.__is_debug_script_exists(args[0]):
                raise DebugScriptNotFoundException(args[0])
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self, package_name, package_version, debug_script_path):
        self._work_folder = str(
            os.path.join(
                debug_script_path, package_name, package_version
            )
        )
        os.makedirs(self._work_folder, exist_ok=True)

    def get_all_debug_scripts(self):
        return os.listdir(self._work_folder)

    def __is_debug_script_exists(self, debug_script_name):
        return os.path.exists(
            os.path.join(self._work_folder, debug_script_name)
        )

    def create_debug_script(self, debug_script_name, content: str | bytes) -> str:
        if self.__is_debug_script_exists(debug_script_name):
            raise DebugScriptAlreadyExistsException(debug_script_name)
        return self.__save_debug_script(debug_script_name, content)

    def create_debug_script_from_template(
            self, debug_script_name, template_name, replace_dict: dict[str, str] = None
    ):
        if self.__is_debug_script_exists(debug_script_name):
            raise DebugScriptAlreadyExistsException(debug_script_name)
        from . import get_template_script_manager
        if replace_dict:
            content = get_template_script_manager().get_replaced_template_content(
                template_name, replace_dict
            )
        else:
            content = get_template_script_manager().get_template_content(template_name)
        return self.__save_debug_script(debug_script_name, content)

    def __save_debug_script(self, debug_script_name, content: str | bytes) -> str:
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        script_path = os.path.join(self._work_folder, debug_script_name)
        with open(script_path, 'w') as debug_script:
            debug_script.write(content)
        return script_path

    @check_debug_script_exists
    def get_debug_script_content(self, debug_script_name) -> str:
        debug_script_path = os.path.join(self._work_folder, debug_script_name)
        with open(debug_script_path, 'r') as debug_script:
            return debug_script.read()

    @check_debug_script_exists
    def update_debug_script(self, debug_script_name, content: str | bytes) -> str:
        self.delete_debug_script(debug_script_name)
        return self.__save_debug_script(debug_script_name, content)

    @check_debug_script_exists
    def delete_debug_script(self, debug_script_name) -> list[str]:
        debug_script_path = os.path.join(self._work_folder, debug_script_name)
        os.remove(debug_script_path)
        return self.get_all_debug_scripts()

    @check_debug_script_exists
    def get_debug_script_path(self, debug_script_name) -> str:
        return os.path.join(self._work_folder, debug_script_name)
