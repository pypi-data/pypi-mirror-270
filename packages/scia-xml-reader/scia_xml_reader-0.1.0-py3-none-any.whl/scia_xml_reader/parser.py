from typing import TypeVar, Type
import xml.etree.ElementTree as ET
from . import parse_info, mapping
from .getters import get_tables, get_table, get_headers, get_objects, get_object_dictionary, \
  get_result_tables, get_rows
from .functions import dictionary_remap, find_indices
from .models import ProjectData, Loadcase, Node, Beam, ResultForce1D, Loadcombination
from .config import CONFIG
from .exceptions import MissingTableError

T = TypeVar("T")


def _parse_table(table: ET.Element, model: Type[T], attribute_mapping: dict[str, str]) -> list[T]:
    """Takes an xml table and parses it into a list of objects."""

    # Not all keys in the mapping are present in the xml by default. 
    headers = get_headers(table)
    output_present = [attr_name for attr_name in attribute_mapping.values() if attr_name in headers]    

    # Retrieve the dictionaries as how they are in the xml
    value_indexes = find_indices(headers, output_present)
    object_elements = get_objects(table)
    obj_dicts = [get_object_dictionary(
        obj, output_present, value_indexes) for obj in object_elements]

    # To create the objects, we need the dictionaries as specified in the mapping
    inverted_mapping = {v: k for k, v in attribute_mapping.items()}
    create_dicts = [dictionary_remap(obj_dict, inverted_mapping)
                    for obj_dict in obj_dicts]

    return [model(**create_dict) for create_dict in create_dicts]

def parse_project_data(root: ET.Element, info: parse_info.ParseInfo = parse_info.ProjectDataParseInfo) -> ProjectData:
    table = get_table(root, info.table_name)

    if not table:
        raise MissingTableError(f"Table with name '{info.table_name}' not found in xml.")
    
    lst = _parse_table(table, model=info.model, attribute_mapping=info.attribute_mapping)
    return lst[0]


def parse_nodes(root: ET.Element, info: parse_info.ParseInfo = parse_info.NodeParseInfo) -> list[Node]:
    table = get_table(root, info.table_name)

    if not table:
        raise MissingTableError(f"Table with name '{info.table_name}' not found in xml.")

    return _parse_table(
        table, model=info.model,
        attribute_mapping=info.attribute_mapping)


def parse_beams(root: ET.Element, info: parse_info.ParseInfo = parse_info.BeamParseInfo) -> list[Beam]:
    table = get_table(root, info.table_name)

    if not table:
        raise MissingTableError(f"Table with name '{info.table_name}' not found in xml.")
    
    return _parse_table(
        table, model=info.model,
        attribute_mapping=info.attribute_mapping)


def parse_loadcases(root: ET.Element, info: parse_info.ParseInfo = parse_info.LoadcaseParseInfo) -> list[Loadcase]:
    # Of course everything from here on isn't in a single table
    tables = get_tables(root, info.table_name)

    if not tables:
        raise MissingTableError(f"Table with name '{info.table_name}' not found in xml.")

    loadcases = []
    for table in tables:
        loadcases.extend(
            _parse_table(
                table, 
                info.model, 
                info.attribute_mapping))
    return loadcases


def parse_loadcombinations(root: ET.Element, info: parse_info.ParseInfo = parse_info.LoadcombinationParseInfo) -> list[Loadcombination]:
    tables = get_tables(root, info.table_name)

    if not tables:
        raise MissingTableError(f"Table with name '{info.table_name}' not found in xml.")

    loadcases = []
    for table in tables:
        loadcases.extend(
            _parse_table(
                table, 
                info.model, 
                info.attribute_mapping))
    return loadcases

def parse_results_force_1d(root: ET.Element, info: parse_info.ParseInfo = parse_info.ResultForce1DParseInfo) -> list[ResultForce1D]:
    
    # Why would the xml be the same for english and dutch systems?
    obj_name = mapping.LANGUAGEMAPPINGRESULTSFORCE1D[CONFIG.language]

    # surprise, the results are not in tables but in nested objects.
    objects = get_result_tables(root, obj_name)

    if not objects:
        raise MissingTableError(f"Table with name '{obj_name}' not found in xml.")

    # Set this for easy access
    MAP = info.attribute_mapping    

    results = []
    for object in objects:     
        # Not all keys in the mapping are present in the xml by default.   
        headers = get_headers(object)
        output_present = [attr_name for attr_name in MAP.values() if attr_name in headers] 

        # Retrieve the dictionaries as how they are in the xml
        value_indices = find_indices(headers, output_present)
        rows = get_rows(object)
        row_dicts = [get_object_dictionary(row, output_present, value_indices) for row in rows]

        # To create the objects, we need the dictionaries as specified in the mapping
        inverted_mapping = {v: k for k, v in MAP.items()}
        create_dicts = [dictionary_remap(row_dict, inverted_mapping)
                        for row_dict in row_dicts]
        
        results.extend([info.model(**create_dict) for create_dict in create_dicts])

    return results


