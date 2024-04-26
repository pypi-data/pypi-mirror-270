from contextlib import contextmanager
import os
import shutil
import tempfile
from typing import List, Optional, Union


@contextmanager
def temporary_directory() -> str:
    try:
        with tempfile.TemporaryDirectory() as tmp_directory_name:
            yield tmp_directory_name
    finally:
        remove_temporary_directory(tmp_directory_name)


@contextmanager
def temporary_file(name: Optional[str] = None, suffix: Optional[str] = None,
                   content: Optional[Union[str, bytes, List[str]]] = None) -> str:
    with temporary_directory() as tmp_directory_name:
        tmp_file_name = os.path.join(tmp_directory_name, name or tempfile.mktemp(dir="")) + (suffix or "")
        with open(tmp_file_name, "wb" if isinstance(content, bytes) else "w") as tmp_file:
            if content is not None:
                tmp_file.write("\n".join(content) if isinstance(content, list) else content)
        yield tmp_file_name


def remove_temporary_directory(tmp_directory_name: str) -> None:
    """
    Removes the given directory, recursively; but ONLY if it is (somewhere) within the system temporary directory.
    """
    def is_temporary_directory(path: str) -> bool:
        try:
            tmpdir = tempfile.gettempdir()
            return os.path.commonpath([path, tmpdir]) == tmpdir and os.path.exists(path) and os.path.isdir(path)
        except Exception:
            return False
    if is_temporary_directory(tmp_directory_name):  # Guard against errant deletion.
        shutil.rmtree(tmp_directory_name)


def create_temporary_file_name(prefix: Optional[str] = None, suffix: Optional[str] = None) -> str:
    """
    Generates and returns the full path to file within the system temporary directory.
    """
    with tempfile.NamedTemporaryFile(prefix=prefix, suffix=suffix, delete=False) as tmp_file:
        tmp_file_name = tmp_file.name
    return tmp_file_name


def remove_temporary_file(tmp_file_name: str) -> bool:
    """
    Removes the given file; but ONLY if it is (somewhere) within the system temporary directory.
    """
    try:
        tmpdir = tempfile.gettempdir()
        if (os.path.commonpath([tmpdir, tmp_file_name]) == tmpdir) and os.path.isfile(tmp_file_name):
            os.remove(tmp_file_name)
            return True
        return False
    except Exception:
        return False
