import typing

from .file_system import G3CoreFileSystem
from .st_parser import STFunction, STFunctionBlock, STIntEnum, STStruct


TSTStructure = typing.TypeVar('TSTStructure')


class SearchResult(typing.NamedTuple, typing.Generic[TSTStructure]):
    """A named tuple to hold search results from the SystemG3Core codebase.

    Attributes:
        path (str): The file path where the structure was found.
        structure (TSTStructure): The structure object found.
    """
    path: str
    """The file path where the structure was found."""
    structure: TSTStructure
    """The structure object found."""


class G3Core:
    """A wrapper around the SystemG3Core codebase."""

    def __init__(self, file_system: G3CoreFileSystem) -> None:
        """Create a new G3Core object from a file system object.

        Args:
            file_system (G3CoreFileSystem): The file system object to use.
        """
        self.file_system = file_system
        """SystemG3Core files' wrapper."""

    @classmethod
    def from_local(cls, path: str) -> typing.Self:
        """Create a new G3Core object from a local directory.

        Args:
            path (str): The path to the local SystemG3Core directory.

        Returns:
            typing.Self: The new G3Core object.
        """
        return cls(G3CoreFileSystem(path))

    @classmethod
    def from_giltab(cls, branch: str = 'master') -> typing.Self:
        """Create a new G3Core object from the GitLab repository.

        Args:
            branch (str, optional): The branch to use as the codebase source.\
                Defaults to 'master'.

        Returns:
            typing.Self: The new G3Core object.
        """
        return cls(G3CoreFileSystem.from_gitlab(branch))

    def find_function_block(
        self,
        fb_name: str,
        search_here_first: str | None = None,
        exclude_private: bool = False
    ) -> SearchResult[STFunctionBlock]:
        """Find a function block in the SystemG3Core files.

        Args:
            fb_name (str): The name of the function block to find.
            search_here_first (str | None, optional): a file path to search\
                first. Defaults to None.
            exclude_private (bool, optional): Whether to exclude private\
                libraries. Defaults to False.

        Raises:
            ValueError: If the function block is not found.

        Returns:
            SearchResult[STFunctionBlock]: A named tuple with the file path\
                and the function block object.
        """

        def find(name: str, path: str) -> SearchResult[STFunctionBlock] | None:
            file = self.file_system.get_fun_file(path)
            try:
                fb = file.get_function_block(name)
                return SearchResult(path, fb)
            except ValueError:
                return None

        if search_here_first:
            if (result := find(fb_name, search_here_first)):
                return result
        for path in self.file_system.file_paths(".fun", exclude_private):
            if (result := find(fb_name, path)):
                return result
        raise ValueError(
            f'Function Block "{fb_name}" was not found in SystemG3Core files.'
            )

    def find_function(
        self,
        f_name: str,
        search_here_first: str | None = None,
        exclude_private: bool = False
    ) -> SearchResult[STFunction]:
        """Find a function in the SystemG3Core files.

        Args:
            f_name (str): The name of the function to find.
            search_here_first (str | None, optional): a file path to search\
                first. Defaults to None.
            exclude_private (bool, optional): Whether to exclude private\
                libraries. Defaults to False.

        Returns:
            SearchResult[STFunction]: A named tuple with the file path and\
                the function object.
        """

        def find(name: str, path: str) -> SearchResult[STFunction] | None:
            file = self.file_system.get_fun_file(path)
            try:
                f = file.get_function(name)
                return SearchResult(path, f)
            except ValueError:
                return None

        if search_here_first:
            if (result := find(f_name, search_here_first)):
                return result
        for path in self.file_system.file_paths(".fun", exclude_private):
            if (result := find(f_name, path)):
                return result
        raise ValueError(
            f'Function "{f_name}" was not found in SystemG3Core files.'
            )

    def find_struct(
        self,
        s_name: str,
        search_here_first: str | None = None,
        exclude_private: bool = False
    ) -> SearchResult[STStruct]:
        """Find a struct in the SystemG3Core files.

        Args:
            s_name (str): The name of the struct to find.
            search_here_first (str | None, optional): a file path to search\
                first. Defaults to None.
            exclude_private (bool, optional): Whether to exclude private\
                libraries. Defaults to False.

        Returns:
            SearchResult[STStruct]: A named tuple with the file path and\
                the struct object.
        """

        def find(name: str, path: str) -> SearchResult[STStruct] | None:
            file = self.file_system.get_typ_file(path)
            try:
                s = file.get_struct(name)
                return SearchResult(path, s)
            except ValueError:
                return None

        if search_here_first:
            if (result := find(s_name, search_here_first)):
                return result
        for path in self.file_system.file_paths(".typ", exclude_private):
            if (result := find(s_name, path)):
                return result
        raise ValueError(
            f'Struct "{s_name}" was not found in SystemG3Core files.'
            )

    def find_enum(
        self,
        e_name: str,
        search_here_first: str | None = None,
        exclude_private: bool = False
    ) -> SearchResult[STIntEnum]:
        """Find an enum in the SystemG3Core files.

        Args:
            e_name (str): The name of the enum to find.
            search_here_first (str | None, optional): a file path to search\
                first. Defaults to None.
            exclude_private (bool, optional): Whether to exclude private\
                libraries. Defaults to False.

        Returns:
            SearchResult[STIntEnum]: A named tuple with the file path and\
                the enum object.
        """

        def find(name: str, path: str) -> SearchResult[STIntEnum] | None:
            file = self.file_system.get_typ_file(path)
            try:
                e = file.get_int_enum(name)
                return SearchResult(path, e)
            except ValueError:
                return None

        if search_here_first:
            if (result := find(e_name, search_here_first)):
                return result
        for path in self.file_system.file_paths(".typ", exclude_private):
            if (result := find(e_name, path)):
                return result
        raise ValueError(
            f'Enum "{e_name}" was not found in SystemG3Core files.'
            )
