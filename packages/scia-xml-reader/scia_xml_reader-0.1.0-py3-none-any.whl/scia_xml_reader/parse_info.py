from dataclasses import dataclass
from . import mapping
from . import models


@dataclass
class ParseInfo:
  table_name: str
  attribute_mapping: dict[str, str]
  model: type

ProjectDataParseInfo = ParseInfo(
  table_name="ProjectData.EP_ProjectData.1",
  attribute_mapping=mapping.PROJECTDATA,
  model = models.ProjectData
)


NodeParseInfo = ParseInfo(
  table_name="EP_DSG_Elements.EP_StructNode.1",
  attribute_mapping=mapping.NODES,
  model=models.Node
)

BeamParseInfo = ParseInfo(
  table_name="EP_DSG_Elements.EP_Beam.1",
  attribute_mapping=mapping.BEAMS,
  model=models.Beam
)

LoadcaseParseInfo = ParseInfo(
  table_name="DataSetScia.EP_LoadCase.1",
  attribute_mapping=mapping.LOADCASES,
  model=models.Loadcase
)

LoadcombinationParseInfo = ParseInfo(
  table_name="DataSetSciaTom.EP_LoadCombi.1",
  attribute_mapping=mapping.LOADCOMBINATIONS,
  model=models.Loadcombination
)

ResultForce1DParseInfo = ParseInfo(
  table_name="BasicResults.10.00.EP_InternalForces1D_Shell.1",
  attribute_mapping=mapping.RESULTSFORCE1D,
  model=models.ResultForce1D
)