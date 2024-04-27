import rwmap._frame as frame
from typing import Union

class KEY:
    empty_tile = "0"

class NAME:
    Ground = "Ground"
    Triggers = "Triggers"
    unitAdd = "unitAdd"

class MAPTYPE:
    skirmish = "skirmish"
    challenge = "challenge"
    survival = "survival"
    mission = "mission"

class FOG:
    NONE = "NONE"
    map = "map"
    los = "los"

class WIN:
    NONE = "NONE"
    mainBuildings = "mainBuildings"
    allUnitsAndBuildings = "allUnitsAndBuildings"
    allBuildings = "allBuildings"
    commandCenter = "commandCenter"
    requiredObjectives = "requiredObjectives"

class COO:
    SIZE_STANDARD = frame.Coordinate(20, 20)

class TYPE:
    tileid = Union[int, tuple[str, int], frame.TagCoordinate]




