import enum
from typing import Type

from localization.localization_data import BaseLocalization
from localization.interface import Localization

localization: Type[BaseLocalization] = Localization.get_localization()


class ArtifactType(enum.Enum):
    FLOWER_OF_LIFE = localization.Artifacts.ArtifactType.FLOWER_OF_LIFE
    PLUME_OF_DEATH = localization.Artifacts.ArtifactType.PLUME_OF_DEATH
    SANDS_OF_EON = localization.Artifacts.ArtifactType.SANDS_OF_EON
    GOBLET_OF_EONOTHEM = localization.Artifacts.ArtifactType.GOBLET_OF_EONOTHEM
    CIRCLET_OF_LOGOS = localization.Artifacts.ArtifactType.CIRCLET_OF_LOGOS


class ArtifactValueType(enum.Enum):
    MIN = "min"
    MAX = "max"


class Stat(enum.Enum):
    HP_FLAT = localization.Artifacts.Stat.HP_FLAT
    ATK_FLAT = localization.Artifacts.Stat.ATK_FLAT
    DEFENCE_FLAT = localization.Artifacts.Stat.DEFENCE_FLAT
    ELEMENTAL_MASTERY = localization.Artifacts.Stat.ELEMENTAL_MASTERY


class PercentStat(enum.Enum):
    HP_PERCENT = localization.Artifacts.PercentStat.HP_PERCENT
    ATK_PERCENT = localization.Artifacts.PercentStat.ATK_PERCENT
    DEFENCE_PERCENT = localization.Artifacts.PercentStat.DEFENCE_PERCENT
    ENERGY_RECHARGE = localization.Artifacts.PercentStat.ENERGY_RECHARGE
    CRIT_DAMAGE = localization.Artifacts.PercentStat.CRIT_DAMAGE
    CRIT_RATE = localization.Artifacts.PercentStat.CRIT_RATE
    HEAL_BONUS = localization.Artifacts.PercentStat.HEAL_BONUS
    ELEMENTAL_DAMAGE_PYRO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.PYRO
    )
    ELEMENTAL_DAMAGE_ANEMO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.ANEMO
    )
    ELEMENTAL_DAMAGE_CRYO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.CRYO
    )
    ELEMENTAL_DAMAGE_ELECTRO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.ELECTRO
    )
    ELEMENTAL_DAMAGE_DENDRO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.DENDRO
    )
    ELEMENTAL_DAMAGE_HYDRO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.HYDRO
    )
    ELEMENTAL_DAMAGE_GEO = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.GEO
    )
    ELEMENTAL_DAMAGE_PHYS = localization.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization.Artifacts.Elements.PHYS
    )


class ArtifactSet(enum.Enum):
    GLADIATORS_FINALE = localization.Artifacts.ArtifactSet.GLADIATORS_FINALE
    WANDERERS_TROUPE = localization.Artifacts.ArtifactSet.WANDERERS_TROUPE
    NOBLESSE_OBLIGE = localization.Artifacts.ArtifactSet.NOBLESSE_OBLIGE
    BLOODSTAINED_CHIVALRY = localization.Artifacts.ArtifactSet.BLOODSTAINED_CHIVALRY
    MAIDEN_BELOVED = localization.Artifacts.ArtifactSet.MAIDEN_BELOVED
    VIRIDESCENT_VENERER = localization.Artifacts.ArtifactSet.VIRIDESCENT_VENERER
