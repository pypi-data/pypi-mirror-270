import re as _re
import typing as _ty

from pathlib_next import Path as _Path


class Reader:

    PATHNAME_REGEX: _re.Pattern = None

    def __init__(self, path: _Path, encoding: str, **kwargs) -> None:
        self.path = path
        self.encoding = encoding

    @classmethod
    def __subclasses__(cls, *, recursive=False) -> list[_ty.Self]:
        subclasess: _ty.Sequence[_ty.Self] = type.__subclasses__(cls)
        if not recursive:
            return subclasess
        return set(subclasess).union(
            [_cls for cls in subclasess for _cls in cls.__subclasses__(recursive=True)]
        )

    def open(self, binary=False):
        return self.path.open(mode="rb" if binary else "r", encoding=self.encoding)

    def read_text(self):
        return self.path.read_text(self.encoding)

    def read_bytes(self):
        return self.path.read_bytes()

    @classmethod
    def get_class_by_name(cls, name: str) -> type[_ty.Self]: ...

    @classmethod
    def is_reader_for_path(cls, path: _Path) -> bool:
        return (
            cls.PATHNAME_REGEX.match(path.name) != None if cls.PATHNAME_REGEX else False
        )

    @classmethod
    def get_class_by_path(cls, path: _Path):
        for scls in cls.__subclasses__(recursive=True):
            if scls.is_reader_for_path(path):
                return scls
        raise NotImplementedError(f"Not reader for {path}")
