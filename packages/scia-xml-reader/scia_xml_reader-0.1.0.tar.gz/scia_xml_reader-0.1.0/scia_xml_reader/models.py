from pydantic import BaseModel

class ProjectData(BaseModel):
  license_user: str
  organization: str
  language: str
  scia_version: str
  date: str
  gravity_acceleration: float
  national_annex: str


class Node(BaseModel):
  name: str
  x: float
  y: float
  z: float

class Beam(BaseModel):
  name: str
  start_node: str
  end_node: str
  x_vector: float | None = None
  y_vector: float | None = None
  z_vector: float | None = None
  lcs_rotation: float | None = None
  cross_section: str
  e_y: str
  e_z: str

class Loadcase(BaseModel):
  name: str
  action_type: str
  description: str
  load_group: str
  load_type: str

class Loadcombination(BaseModel):
  name: str
  type: str

class ResultForce1D(BaseModel):
  member: str
  dx: float
  loadcase: str
  N: float
  V_y: float
  V_z: float
  M_x: float
  M_y: float
  M_z: float
  V_r: float
