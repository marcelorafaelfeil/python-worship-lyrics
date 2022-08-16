import os
import sys

basedir = os.path.dirname(os.path.realpath(sys.argv[0]))


class PathUtils:
    @staticmethod
    def icon(icon_name: str) -> str:
        return os.path.join(basedir, 'assets', 'icons', icon_name)

    @staticmethod
    def template(template_name: str) -> str:
        return os.path.join(basedir, 'assets', 'template', template_name)
