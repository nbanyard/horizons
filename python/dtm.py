import os
import zipfile
import re

import references

NUMBERS_RE = re.compile(r'^[0-9. -]*$')

class DTM:
    def __init__(self, zippath):
        self._create_cache_dir(zippath)
        self._open_zipfile(zippath)

        self.heights = {}

    def _create_cache_dir(self, zippath):
        if zippath.endswith('.zip'):
            self.cache_dir = zippath[:-4]
        else:
            self.cache_dir = zippath + '.d'

        if not os.path.isdir(self.cache_dir):
            os.mkdir(self.cache_dir)

    def _cache_filename(self, two_fig):
        return os.path.join(self.cache_dir, two_fig.lower() + '.zip')

    def _open_zipfile(self, zippath):
        self.zipfile = zipfile.ZipFile(zippath)
        self.namelist = self.zipfile.namelist()

    def get_height(self, eastings, northings):
        two_fig = references.to_osref((eastings, northings), 2)

        if two_fig in self.heights:
            heights = self.heights[two_fig]
        else:
            cache_name = self._cache_filename(two_fig)

            if not os.path.isfile(cache_name):
                in_zip_name_re = re.compile(r'^.*\b%s/%s_.*\.zip$' % (two_fig[:2], two_fig), re.I)
                in_zip_name = next(n for n in self.namelist if in_zip_name_re.match(n))

                with self.zipfile.open(in_zip_name) as zip_stream:
                    with open(cache_name, 'w') as cache_stream:
                        data = zip_stream.read()
                        while len(data) > 0:
                            cache_stream.write(data)
                            data = zip_stream.read()

            lines = []
            with zipfile.ZipFile(cache_name) as cached_zip:
                cached_namelist = cached_zip.namelist()
                asc_name = next(n for n in cached_namelist if n.endswith('.asc'))
                with cached_zip.open(asc_name) as cached_stream:
                    more_data = cached_stream.readlines()
                    while len(more_data) > 0:
                        lines = lines + more_data
                        more_data = cached_stream.readlines()
            heights = [[float(word) for word in line.split()]
                       for line in lines if NUMBERS_RE.match(line)
                      ]
            self.heights[two_fig] = heights

        l = 200 - northings % 10000 // 50
        w = eastings % 10000 // 50

        return heights[l][w]
