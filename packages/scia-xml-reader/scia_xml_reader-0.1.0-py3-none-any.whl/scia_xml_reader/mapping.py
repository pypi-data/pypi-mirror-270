from typing import TypeAlias
from .config import Language

MapDict: TypeAlias = dict[str, str]

PROJECTDATA: MapDict = {
    'license_user': 'Licence user',  # ..yes it's a typo in the xml
    'organization': 'Organization',
    'language': 'National code',
    'scia_version': 'Version',
    'date': 'Date',
    'gravity_acceleration': 'Acceleration of gravity',
    'national_annex': 'National annex',
}


NODES: MapDict = {
    'name': 'Name',
    'x': 'Coord X',
    'y': 'Coord Y',
    'z': 'Coord Z'
}

BEAMS: MapDict = {
    'name': 'Name',
    'start_node': 'Beg. node',
    'end_node': 'End node',
    'x_vector': 'X',
    'y_vector': 'Y',
    'z_vector': 'Z',
    'lcs_rotation': 'LCS Rotation',
    'cross_section': 'Cross-section',
    'e_y': 'ey',
    'e_z': 'ez'
}

LOADCASES: MapDict = {
    'name': 'Name',
    'action_type': 'Action type',
    'description': 'Description',
    'load_group': 'Load group',
    'load_type': 'Load type'
}

LOADCOMBINATIONS: MapDict = {
    'name': 'Name',
    'type': 'Type'
}

RESULTSFORCE1D: MapDict = {
    'member': 'Name',
    'dx': 'dx',
    'loadcase': 'Case',
    'N': 'N',
    'V_y': 'V_y',
    'V_z': 'V_z',
    'M_x': 'M_x',
    'M_y': 'M_y',
    'M_z': 'M_z',
    'V_r': 'V_r'
}

LANGUAGEMAPPINGRESULTSFORCE1D: MapDict = {
    Language.EN: "1D internal forces",
    Language.NL: "Interne 1D-krachten"
}
