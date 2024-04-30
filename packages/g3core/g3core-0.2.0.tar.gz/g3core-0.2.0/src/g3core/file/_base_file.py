import re
import functools

from dataclasses import dataclass


# the function below is not a part of the "BaseFile" class because it
# is decorated with "functools.cache", and it is better to use this decorator
# on functions rather than methods.

@functools.cache
def extract_from_file_contents(
    file_contents: str,
    structure_name: str,
    structure_type: str,
    search_pattern: str
) -> str:
    """Extract an ST code block from a file contents.

    Args:
        file_contents (str): The contents of the file to search.
        structure_name (str): The name of the code structure to search for.
        structure_type (str): The type of the structure to search for,\
            e.g., "Function Block", "Function", "Struct", etc.
        search_pattern (str): The regex pattern to search the structure with.

    Raises:
        ValueError: If the structure is not found in the file.

    Returns:
        str: The extracted code block.
    """
    contents = re.search(
        search_pattern, file_contents, flags=re.DOTALL | re.MULTILINE
        )
    if contents:
        return contents.group(1)
    raise ValueError(
        f'{structure_type} "{structure_name}" was not found in the file.'
        )


@dataclass(frozen=True)
class BaseFile:
    """Base class for SystemG3Core file types.

    Attributes:
        contents (str): The contents of the file.
    """
    contents: str
    """The contents of the file."""

    def _get_structure(
        self,
        structure_name: str,
        structure_type: str,
        search_pattern: str
    ) -> str:
        """Utility method to extract a code block from the file contents.
        Wrapper around the "extract_from_file_contents" function.

        Args:
            structure_name (str): The name of the code structure to search for.
            structure_type (str): The type of the structure to search for,\
                e.g., "Function Block", "Function", "Struct", etc.
            search_pattern (str): The regex pattern to search the structure\
                with.

        Returns:
            str: The extracted code block.
        """
        return extract_from_file_contents(
            self.contents, structure_name, structure_type, search_pattern
            )
