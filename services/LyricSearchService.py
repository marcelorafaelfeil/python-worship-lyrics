import unidecode

from controller.core import ApplicationContext


class LyricSearchService:
    def __init__(self, text_to_search: str):
        self.lyrics_services = ApplicationContext.lyrics_service
        self.text_to_search = text_to_search
        self.lyrics_list = self.lyrics_services.data

    def search(self):
        self.search_by_name()

    def search_by_name(self):
        result = []
        lyrics_list = self.lyrics_list

        for lyric in lyrics_list:
            name: str = unidecode.unidecode(lyric.name)
            search: str = unidecode.unidecode(self.text_to_search)

            name = name.lower()
            search = search.lower()

            if name.find(search) >= 0:
                result.append(lyric)

        return result

    def search_by_author(self):
        result = []
        lyrics_list = self.lyrics_list

        for lyric in lyrics_list:
            author: str = unidecode.unidecode(lyric.author)
            search: str = unidecode.unidecode(self.text_to_search)

            if author.find(search) >= 0:
                result.append(lyric)

        return result

    def search_by_lyric(self):
        result = []
        lyrics_list = self.lyrics_list

        for lyric in lyrics_list:
            path: str = lyric.path

            f = open(path, 'r', encoding='utf-8')

            content: str = unidecode.unidecode(f.read().lower())
            content = content.replace('\n', ' ').replace('  ', ' ')

            f.close()

            text_to_search: str = unidecode.unidecode(self.text_to_search)
            text_to_search = text_to_search.lower()
            text_to_search = text_to_search.replace('\n', ' ').replace('  ', ' ')

            if content.find(text_to_search) >= 0:
                result.append(lyric)

        return result

