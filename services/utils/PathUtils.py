import os
import sys

basedir = os.path.dirname(os.path.realpath(sys.argv[0]))


class PathUtils:
    @staticmethod
    def icon(icon_name: str) -> str:
        print(os.path.join(basedir, 'assets', 'icons', icon_name))
        return os.path.join(basedir, 'assets', 'icons', icon_name)

    @staticmethod
    def template(template_name: str) -> str:
        return os.path.join(basedir, 'assets', 'template', template_name)

    @staticmethod
    def settings(file_name: str) -> str:
        return os.path.join(basedir, 'settings', file_name)

    @staticmethod
    def validatePath(path: str):
        last_char = path[-1]

        if last_char != '/':
            path += '/'

        return path
