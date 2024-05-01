from pathlib import Path
import xml.etree.ElementTree as ET
from typing import TypeVar


def dictionary_remap(original_dict: dict, mapping: dict[str, str]) -> dict:
    """Modifies the keys of the original dictionary according to the given mapping."""
    return {mapping[key]: value for key, value in original_dict.items()}


T = TypeVar("T")


def find_indices(all_items: list[T], item_subset: list[T]) -> list[int]:
    """Takes a list and a subset of that list. For each item in the subset the index is returned."""
    return [all_items.index(item) for item in item_subset]


def read_xml(xml_path: Path) -> ET.Element:
    """Reads the given path as an root Element."""
    tree = ET.parse(xml_path)
    return tree.getroot()