import re
from fancy_printer import FancyPrinter
from typing import Dict


fancy_print = FancyPrinter()


_re_json_state = re.compile(r"{.+[:,].+}|\[.+[,:].+\]", re.DOTALL | re.MULTILINE)


def get_json_object(dirty_str: str) -> str:
    return _re_json_state.findall(dirty_str)[0]


_re_xml_state = re.compile(r"<(\w+)>(.*?)<\/\1>", re.DOTALL | re.MULTILINE)


def get_xml_tags(dirty_str: str) -> Dict[str, str]:
    matches = _re_xml_state.findall(dirty_str)
    return {match[0]: match[1].strip() for match in matches}
