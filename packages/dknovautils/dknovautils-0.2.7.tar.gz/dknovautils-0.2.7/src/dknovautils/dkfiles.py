from __future__ import annotations

from dknovautils.commons import *

import pathlib


_debug = False


class DkFile(object):
    def __init__(self, pathstr: str) -> None:
        self.pathstr = str(pathstr)

        self.path = Path(pathstr)

    def __key(self) -> Any:
        return self.path

    def __hash__(self) -> int:
        return hash(self.__key())

    def __eq__(self, other:Any) -> Any:
        if isinstance(other, DkFile):
            return self.__key() == other.__key()
        return NotImplemented

    @property
    def basename(self) -> str:
        return os.path.basename(self.path)

    @property
    def filesize(self) -> int:
        return getsize(self.path)

    @property
    def dirname(self) -> str:
        return os.path.dirname(self.path)

    @property
    def extension(self) -> str:
        """包括点号 比如 .txt 如果没有扩展名 则返回空串 """
        # function to return the file extension
        file_extension = self.path.suffix
        return file_extension

    def exists(self) -> bool:
        return self.path.exists()

    def is_file(self) -> bool:
        return self.path.is_file()

    def is_dir(self) -> bool:
        return self.path.is_dir()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.path)

    @staticmethod
    def clear_dir(folder: str) -> None:
        """

        https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder

        """
        import os, shutil

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                iprint("Failed to delete %s. Reason: %s" % (file_path, e))

    @staticmethod
    def file_md5(f: str, md5Cache: Dict[str, str] | None = None) -> str:
        # todo 更换为合理的计算方式

        if md5Cache is None:
            md5Cache = {}

        if f in md5Cache:
            r = md5Cache[f]
            assert len(r) == 32
            return r
        else:
            iprint_debug(f"gen md5 {f}")
            bs = Path(f).read_bytes()
            md5 = hashlib.md5()
            # md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
            md5.update(bs)
            r = md5.hexdigest().lower()
            assert len(r) == 32

            md5Cache[f] = r
            return r

    @staticmethod
    def listdir(d: str) -> List[DkFile]:
        fs = [DkFile(join(d, f)) for f in os.listdir(d)]
        # fs=[DkFile(f) for f in fs]
        return fs

    @staticmethod
    def file_sha1(f: str) -> str:
        import hashlib

        bs = Path(f).read_bytes()
        md5 = hashlib.sha1()
        # md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
        md5.update(bs)
        r = md5.hexdigest().lower()
        assert len(r) == 32
        return r


class DkPyFiles(object):
    pass


if __name__ == "__main__":
    print("OK")
