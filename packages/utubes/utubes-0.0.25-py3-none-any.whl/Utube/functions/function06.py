import requests
from bs4 import BeautifulSoup
#======================================================================

class SMessages:
    def __init__(self, **kwargs):
        self.errors = kwargs.get("errors", None)
        self.filelink = kwargs.get("filelink", None)

#======================================================================

class GDlinks:

    async def mediafire(filelink):
        try:
            uris = str(filelink)
            cors = requests.get(uris).content
            page = BeautifulSoup(cors, 'lxml')
            info = page.find('a', {'aria-label': 'Download file'})
            oung = info.get('href')
            return SMessages(filelink=oung)
        except Exception as errors:
            return SMessages(filelink=filelink, errors=errors)

#======================================================================
