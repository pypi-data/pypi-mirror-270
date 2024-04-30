from dataclasses import dataclass

from ..st_parser import STFunction, STFunctionBlock
from ._base_file import BaseFile


@dataclass(frozen=True)
class FunFile(BaseFile):
    """A wrapper around a `.fun` SystemG3Core file.

    Attributes:
        contents (str): The contents of the file.
    """

    def get_function_block(self, fb_name: str) -> STFunctionBlock:
        """Get a function block wrapper from the file.

        Args:
            fb_name (str): The name of the function block to get.

        Returns:
            STFunctionBlock: The function block wrapper object.
        """
        fb_contents = self._get_structure(
            structure_name=fb_name,
            structure_type='Function block',
            search_pattern=(
                f'(^\\s*FUNCTION_BLOCK\\s+{fb_name}\\s+.*?END_FUNCTION_BLOCK)'
                )
            )
        return STFunctionBlock(fb_contents)

    def get_function(self, func_name: str) -> STFunction:
        """Get a function wrapper from the file.

        Args:
            func_name (str): The name of the function to get.

        Returns:
            STFunction: The function wrapper object.
        """
        f_contents = self._get_structure(
            structure_name=func_name,
            structure_type='Function',
            search_pattern=(
                f'(^\\s*FUNCTION\\s+{func_name}\\s+.*?END_FUNCTION)'
                )
            )
        return STFunction(f_contents)
