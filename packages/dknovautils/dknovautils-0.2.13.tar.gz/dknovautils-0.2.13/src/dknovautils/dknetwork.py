from dknovautils import commons, iprint_debug, iprint_warn, AT  # type:ignore
from dknovautils.commons import *

import urllib3

http = urllib3.PoolManager(timeout=5.0)


class DkNetwork:

    @staticmethod
    def get_url_simple_str(url: str) -> str | None:
        try:
            r = http.request("GET", url)
            # print(json.loads(r.data.decode('utf-8')))
            s = r.data.decode("utf-8")
            assert isinstance(s, str)
            return s
        except Exception as e:
            iprint_debug(e)
            return None
