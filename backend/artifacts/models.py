from typing import List

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


class Artifact(BaseModel):
    name: str
    type: ArtifactType
    set: ArtifactSet
    main_stat: ArtifactMainStat
    sub_stats: List[ArtifactSubStat]
    level: int = 0
