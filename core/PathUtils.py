

class PathUtils:
    @staticmethod
    def validatePath(path: str):
        last_char = path[-1]

        if last_char != '/':
            path += '/'

        return path
