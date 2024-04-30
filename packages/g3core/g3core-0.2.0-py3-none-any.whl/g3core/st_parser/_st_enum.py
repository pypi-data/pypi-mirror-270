import itertools
import re

from dataclasses import dataclass


@dataclass
class STIntEnum:
    """Structured Text integer enumeration.

    Attributes:
        contents (str): The contents of the enumeration.
    """
    contents: str
    """The contents of the enumeration."""

    def normalize_indentation(
        self, indent: int = 4, indent_char: str = ' '
    ) -> str:
        """Normalize the indentation of the enumeration contents.

        Args:
            indent (int, optional): The number of space characters to use\
                for each indentation level. Defaults to 4.
            indent_char (str, optional): The character to use for indentation.\
                Defaults to ' ' (whitespace character).

        Returns:
            str: The enumeration contents with normalized indentation.
        """
        lines = self.contents.split('\n')
        first_line = lines.pop(0).strip()
        last_line = lines.pop(-1).strip()
        formatted_lines = [first_line]
        for line in lines:
            stripped = line.strip()
            formatted_lines.append(indent_char * 1 * indent + stripped)
        formatted_lines.append(last_line)
        return "\n".join(formatted_lines)

    @property
    def name(self) -> str:
        """The name of the enumeration."""
        name = re.search(r"^\s*(\w+)\s*:", self.contents)
        if not name:
            raise TypeError('Cannot parse the name of the enum.')
        return name.group(1)

    @property
    def members(self) -> dict[str, int]:
        """The members of the enumeration."""
        members_pattern = r"\(\s*(.*?)\s*\)"
        members_section = re.search(members_pattern, self.contents, re.DOTALL)
        if not members_section:
            raise TypeError('Cannot parse the members of the enum.')
        member_lines = members_section.group(1).split(',')
        members = {}
        counter = itertools.count()
        for line in member_lines:
            parts = line.split(":=")
            member_name = parts[0].strip()
            if len(parts) == 2:
                member_value = int(parts[1].strip(' ,'))
            else:
                member_value = next(counter)
            members[member_name] = member_value
        return members
