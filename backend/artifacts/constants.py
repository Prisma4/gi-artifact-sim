import enum
from typing import Type

from localization.enums import BaseLocalization
from localization.interface import Localization

localization_enum: Type[BaseLocalization] = Localization.get_localization_enum()


class ArtifactType(enum.Enum):
    FLOWER_OF_LIFE = localization_enum.Artifacts.ArtifactType.FLOWER_OF_LIFE
    PLUME_OF_DEATH = localization_enum.Artifacts.ArtifactType.PLUME_OF_DEATH
    SANDS_OF_EON = localization_enum.Artifacts.ArtifactType.SANDS_OF_EON
    GOBLET_OF_EONOTHEM = localization_enum.Artifacts.ArtifactType.GOBLET_OF_EONOTHEM
    CIRCLET_OF_LOGOS = localization_enum.Artifacts.ArtifactType.CIRCLET_OF_LOGOS


class ArtifactValueType(enum.Enum):
    MIN = "min"
    MAX = "max"


class Stat(enum.Enum):
    HP_FLAT = localization_enum.Artifacts.Stat.HP_FLAT
    ATK_FLAT = localization_enum.Artifacts.Stat.ATK_FLAT
    DEFENCE_FLAT = localization_enum.Artifacts.Stat.DEFENCE_FLAT
    ELEMENTAL_MASTERY = localization_enum.Artifacts.Stat.ELEMENTAL_MASTERY


class PercentStat(enum.Enum):
    HP_PERCENT = localization_enum.Artifacts.PercentStat.HP_PERCENT
    ATK_PERCENT = localization_enum.Artifacts.PercentStat.ATK_PERCENT
    DEFENCE_PERCENT = localization_enum.Artifacts.PercentStat.DEFENCE_PERCENT
    ENERGY_RECHARGE = localization_enum.Artifacts.PercentStat.ENERGY_RECHARGE
    CRIT_DAMAGE = localization_enum.Artifacts.PercentStat.CRIT_DAMAGE
    CRIT_RATE = localization_enum.Artifacts.PercentStat.CRIT_RATE
    HEAL_BONUS = localization_enum.Artifacts.PercentStat.HEAL_BONUS
    ELEMENTAL_DAMAGE_PYRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.PYRO
    )
    ELEMENTAL_DAMAGE_ANEMO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.ANEMO
    )
    ELEMENTAL_DAMAGE_CRYO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.CRYO
    )
    ELEMENTAL_DAMAGE_ELECTRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.ELECTRO
    )
    ELEMENTAL_DAMAGE_DENDRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.DENDRO
    )
    ELEMENTAL_DAMAGE_HYDRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.HYDRO
    )
    ELEMENTAL_DAMAGE_GEO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.GEO
    )
    ELEMENTAL_DAMAGE_PHYS = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.format(
        localization_enum.Artifacts.Elements.PHYS
    )


class ArtifactSet(enum.Enum):
    GLADIATORS_FINALE = localization_enum.Artifacts.ArtifactSet.GLADIATORS_FINALE
    WANDERERS_TROUPE = localization_enum.Artifacts.ArtifactSet.WANDERERS_TROUPE
    NOBLESSE_OBLIGE = localization_enum.Artifacts.ArtifactSet.NOBLESSE_OBLIGE
    BLOODSTAINED_CHIVALRY = localization_enum.Artifacts.ArtifactSet.BLOODSTAINED_CHIVALRY
    MAIDEN_BELOVED = localization_enum.Artifacts.ArtifactSet.MAIDEN_BELOVED
    VIRIDESCENT_VENERER = localization_enum.Artifacts.ArtifactSet.VIRIDESCENT_VENERER
