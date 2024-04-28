import os

from ._exceptions import TemplateNotFoundException, TemplateAlreadyExistsException, \
    ReplaceDictMustStartWithDollarSignException


class TemplateManager:
    @staticmethod
    def check_template_exists(func):
        def wrapper(self, *args, **kwargs):
            if not self.__is_template_exists(args[0]):
                raise TemplateNotFoundException(args[0])
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self, template_dir):
        self.template_dir = template_dir
        os.makedirs(template_dir, exist_ok=True)

    def get_all_templates(self) -> list[str]:
        return os.listdir(self.template_dir)

    def __is_template_exists(self, template_name) -> bool:
        return os.path.exists(
            os.path.join(self.template_dir, template_name)
        )

    @staticmethod
    def __is_file_exists(file_path) -> bool:
        return os.path.exists(file_path)

    def create_template(self, template_name: str, content: str | bytes) -> str:
        if self.__is_template_exists(template_name):
            raise TemplateAlreadyExistsException(template_name)
        return self.__save_template(template_name, content)

    @check_template_exists
    def get_template_content(self, template_name) -> str:
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, 'r') as f:
            return f.read()

    @check_template_exists
    def update_template(self, template_name, content: str | bytes) -> str:
        self.delete_template(template_name)
        return self.__save_template(template_name, content)

    def __save_template(self, template_name, content: str | bytes) -> str:
        template_path = os.path.join(self.template_dir, template_name)
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        with open(template_path, 'w') as f:
            f.write(content)
        return str(template_path)

    @check_template_exists
    def delete_template(self, template_name) -> list[str]:
        template_path = os.path.join(self.template_dir, template_name)
        os.remove(template_path)
        return self.get_all_templates()

    @check_template_exists
    def get_template_path(self, template_name) -> str:
        return str(os.path.join(self.template_dir, template_name))

    @check_template_exists
    def get_replaced_template_content(
            self, template_name, replace_dict: dict[str, str]
    ) -> str:
        template_content = self.get_template_content(template_name)
        for key, value in replace_dict.items():
            if not key.startswith('$'):
                raise ReplaceDictMustStartWithDollarSignException(key)
            template_content = template_content.replace(key, value)
        return template_content
