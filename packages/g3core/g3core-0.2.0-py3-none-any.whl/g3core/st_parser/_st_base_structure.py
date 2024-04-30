import re

from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from ._st_var import STVariable


@dataclass
class STBaseStructure(ABC):
    """Base class for all structured text structures.

    Attributes:
        contents (str): The contents of the structured text structure.
    """
    contents: str
    """The contents of the structured text structure."""

    def __str__(self) -> str:
        return self.contents

    def normalize_indentation(
        self, indent: int = 4, indent_char: str = ' '
    ) -> str:
        """Normalize the indentation of the structured text contents.

        Args:
            indent (int, optional): The number of space characters to use\
                for each indentation level. Defaults to 4.
            indent_char (str, optional): The character to use for indentation.\
                Defaults to ' ' (whitespace character).

        Returns:
            str: The structured text contents with normalized indentation.
        """
        lines = self.contents.split('\n')
        first_line = lines.pop(0).strip()
        last_line = lines.pop(-1).strip()
        formatted_lines = [first_line]
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("VAR") or stripped.startswith("END_VAR"):
                formatted_lines.append(indent_char * 1 * indent + stripped)
            else:
                formatted_lines.append(indent_char * 2 * indent + stripped)
        formatted_lines.append(last_line)
        return "\n".join(formatted_lines)

    def _parse_section(
        self, section_start_kw: str, section_end_kw: str
    ) -> list[STVariable]:
        """Parse a section of structured text for variables.

        Args:
            section_start_kw (str): The first keyword of the section.
            section_end_kw (str): The last keyword of the section.

        Returns:
            list[STVariable]: The list of variables found in the section.
        """
        pattern = f'{section_start_kw}(.*?){section_end_kw}'
        section = re.search(pattern, self.contents, re.DOTALL)
        if not section:
            return []
        vars_matches = re.findall(
            r"(\w+) : ([^\:=]+)(?:(?: := (.*?))?;)(?:\s*\(\*(.*?)\*\))?",
            section.group(1)
            )
        return [
            STVariable(
                name=vm[0],
                dtype=vm[1],
                value=vm[2] if vm[2] else None,
                default=vm[2] if vm[2] else None,
                comment=vm[3] if vm[3] else None
                )
            for vm in vars_matches
            ]

    @cached_property
    def name(self) -> str:
        """The name of the structured text structure."""
        return self._extract_name()

    @abstractmethod
    def _extract_name(self) -> str:
        """Implement this method to extract the name of the structured text
        structure from the contents.
        """
        ...

    @abstractmethod
    def _instantiate(self, *args, **kwargs) -> str:
        """Implement this method to generate a string written in the structured
        text language to instantiate the structured text structure.
        """
        ...

    def instantiate(self, *args, **kwargs) -> str:
        """Generate a string written in the structured text language to
        instantiate the structured text structure.

        Returns:
            str: The string to instantiate the structured text structure.
        """
        return self._instantiate(*args, **kwargs)
