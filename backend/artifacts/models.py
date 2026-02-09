from typing import List, Optional

from pydantic import BaseModel

from artifacts.constants import ArtifactType, PercentStat, Stat, ArtifactSet


class ArtifactMainStat(BaseModel):
    stat: Stat | PercentStat
    value: float
    is_percent: bool = False


class ArtifactSubStat(BaseModel):
    stat: Stat | PercentStat
    value: float
    is_percent: bool = False
    is_active: bool = True


class ProcLog(BaseModel):
    substat: ArtifactSubStat
    increased_by: float


class Artifact(BaseModel):
    name: str
    type: ArtifactType
    set: ArtifactSet
    main_stat: ArtifactMainStat
    substats: List[ArtifactSubStat]
    level: int = 0

    logs: List[ProcLog] = []
