from typing import Any
import xml.etree.ElementTree as ET
from .config import NS


def get_tables(element: ET.Element, table_t: str) -> list[ET.Element]:
    return element.findall(f".//scia:table[@t='{table_t}']", NS)


def get_table(element: ET.Element, table_t: str) -> ET.Element:
    return element.find(f".//scia:table[@t='{table_t}']", NS)


def get_headers(element: ET.Element) -> list[str]:
    header_element = element.find('.//scia:h', NS)
    if not header_element:
        raise ValueError(f"Element '{element}' has no headers.")
    return [h.attrib['t'] for h in header_element]


def get_objects(element: ET.Element) -> list[ET.Element]:
    return element.findall('.//scia:obj', NS)


def get_object_dictionary(element: ET.Element, keys: list[str], indexes: list[int]) -> dict:
    object_dict = dict()
    for index, key in zip(indexes, keys):
        object_dict[key] = get_attrib_value(element[index].attrib)
    return object_dict


def get_attrib_value(attrib: dict, possible_keys: list[str] = ['t', 'v', 'n']) -> Any:
    """
    If the value represents an enum value, it's stored in the 't' attribute. If the value links to another object, 
    the value is stored as a string in the 'n' attribute. If it's a simple data type, 
    it's stored in the 'v' attribute.
    """
    for key in possible_keys:
        val = attrib.get(key, False)
        if val:
            return val


def get_result_tables(element: ET.Element, object_nm: str) -> list[ET.Element]:
    return element.findall(f".//scia:obj[@nm='{object_nm}']", NS)

def get_rows(element: ET.Element) -> list[ET.Element]:
    return element.findall('.//scia:row', NS)

