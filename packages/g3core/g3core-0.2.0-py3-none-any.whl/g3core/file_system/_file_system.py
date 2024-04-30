import os
import functools
import logging
import typing

from git import Repo
from platformdirs import user_cache_dir

from ..file._fun_file import FunFile
from ..file._typ_file import TypFile


logger = logging.getLogger('g3core.file_system')


# the function below is not a part of the "G3CoreFileSystem" class because it
# is decorated with "functools.cache", and it is better to use this decorator
# on functions rather than methods.

@functools.cache
def get_file_contents(filepath: str) -> str:
    """Read the contents of a local file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


class G3CoreFileSystem:
    """Utility class for loading SystemG3Core files.

    Attributes:
        PRIVATE_LIBRARIES (list[str]): The list of private library names.
        REPO_URL (str): The URL of the SystemG3Core repository.
    """
    PRIVATE_LIBRARIES = ['_BR']
    """The list of private library names."""
    REPO_URL = "https://gitlab.elektroline.cz/plc/SystemG3Core.git"
    """The URL of the SystemG3Core repository."""

    def __init__(self, path: str) -> None:
        """Create a new G3CoreFileSystem instance.

        Args:
            path (str): The path to the local SystemG3Core directory.
        """
        self.path = path
        """The path to the local SystemG3Core directory."""
        self._fun_files: dict[str, FunFile] = {}
        """Private cache for `.fun` file objects."""
        self._typ_files: dict[str, TypFile] = {}
        """Private cache for `.typ` file objects."""

    @classmethod
    def from_gitlab(cls, branch: str = 'master') -> typing.Self:
        """Create a new G3CoreFileSystem instance from the GitLab repository.

        Args:
            branch (str, optional): The branch to use as the codebase source.\
                Defaults to 'master'.

        Returns:
            typing.Self: The new G3CoreFileSystem instance.
        """
        path = user_cache_dir('g3core')
        if os.path.exists(path):
            with Repo(path) as repo:
                logger.info("Fetching latest SystemG3Core changes")
                repo.git.fetch(all=True)
                repo.git.checkout(branch)
                if repo.is_dirty():
                    repo.git.reset('--hard')
                repo.git.pull('origin', branch)
                logger.info(
                    "SystemG3Core has been updated to the latest on branch: "
                    "%s", branch
                    )
        else:
            logger.info("Cloning SystemG3Core from %s", cls.REPO_URL)
            with Repo.clone_from(cls.REPO_URL, to_path=path, branch=branch):
                pass
            logger.info(
                "SystemG3Core has been cloned and checked out on branch: "
                "%s", branch
                )
        return cls(path)

    @classmethod
    def _is_dirpath_private(cls, dirpath: str) -> bool:
        """Check if a directory path is a private library.

        Args:
            dirpath (str): The directory path to check.

        Returns:
            bool: False if the directory path is not a private library or\
                if the private libraries list is empty. True otherwise.
        """
        if not cls.PRIVATE_LIBRARIES:
            return False
        return any(lib in dirpath for lib in cls.PRIVATE_LIBRARIES)

    def file_paths(
        self, ext: str | None = None, exclude_private: bool = True
    ) -> typing.Iterator[str]:
        """Iterate over the file paths in the SystemG3Core directory.

        Args:
            ext (str | None, optional): The file extension to filter by.\
                If None, all files are returned. Defaults to None.
            exclude_private (bool, optional): Whether to exclude private\
                libraries in the search. Defaults to True.

        Returns:
            typing.Iterator[str]: The file paths.
        """
        for dirpath, _, filenames in os.walk(self.path):
            if '.git' in dirpath:
                continue
            if self._is_dirpath_private(dirpath) and not exclude_private:
                continue
            for filename in filenames:
                if ext is None or filename.endswith(ext):
                    yield os.path.join(dirpath, filename)

    def get_fun_file(self, path: str) -> FunFile:
        """Get a `.fun` file wrapper for a file path.

        Args:
            path (str): The path to the `.fun` file.

        Returns:
            FunFile: The `.fun` file wrapper object.
        """
        if path not in self._fun_files:
            self._fun_files[path] = FunFile(get_file_contents(path))
        return self._fun_files[path]

    def get_typ_file(self, path: str) -> TypFile:
        """Get a `.typ` file wrapper for a file path.

        Args:
            path (str): The path to the `.typ` file.

        Returns:
            TypFile: The `.typ` file wrapper object.
        """
        if path not in self._typ_files:
            self._typ_files[path] = TypFile(get_file_contents(path))
        return self._typ_files[path]
