import enum
from typing import Type

from localization.enums import BaseLocalization
from localization.interface import Localization

localization_enum: Type[BaseLocalization] = Localization.get_localization_enum()


class ArtifactType(enum.StrEnum):
    FLOWER_OF_LIFE = localization_enum.Artifacts.ArtifactType.FLOWER_OF_LIFE.value
    PLUME_OF_DEATH = localization_enum.Artifacts.ArtifactType.PLUME_OF_DEATH.value
    SANDS_OF_EON = localization_enum.Artifacts.ArtifactType.SANDS_OF_EON.value
    GOBLET_OF_EONOTHEM = localization_enum.Artifacts.ArtifactType.GOBLET_OF_EONOTHEM.value
    CIRCLET_OF_LOGOS = localization_enum.Artifacts.ArtifactType.CIRCLET_OF_LOGOS.value


class ArtifactValueType(enum.StrEnum):
    MIN = "min"
    MAX = "max"


class Stat(enum.StrEnum):
    HP_FLAT = localization_enum.Artifacts.Stat.HP_FLAT.value
    ATK_FLAT = localization_enum.Artifacts.Stat.ATK_FLAT.value
    DEFENCE_FLAT = localization_enum.Artifacts.Stat.DEFENCE_FLAT.value
    ELEMENTAL_MASTERY = localization_enum.Artifacts.Stat.ELEMENTAL_MASTERY.value


class PercentStat(enum.StrEnum):
    HP_PERCENT = localization_enum.Artifacts.PercentStat.HP_PERCENT.value
    ATK_PERCENT = localization_enum.Artifacts.PercentStat.ATK_PERCENT.value
    DEFENCE_PERCENT = localization_enum.Artifacts.PercentStat.DEFENCE_PERCENT.value
    ENERGY_RECHARGE = localization_enum.Artifacts.PercentStat.ENERGY_RECHARGE.value
    CRIT_DAMAGE = localization_enum.Artifacts.PercentStat.CRIT_DAMAGE.value
    CRIT_RATE = localization_enum.Artifacts.PercentStat.CRIT_RATE.value
    HEAL_BONUS = localization_enum.Artifacts.PercentStat.HEAL_BONUS.value
    ELEMENTAL_DAMAGE_PYRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.PYRO.value
    )
    ELEMENTAL_DAMAGE_ANEMO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.ANEMO.value
    )
    ELEMENTAL_DAMAGE_CRYO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.CRYO.value
    )
    ELEMENTAL_DAMAGE_ELECTRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.ELECTRO.value
    )
    ELEMENTAL_DAMAGE_DENDRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.DENDRO.value
    )
    ELEMENTAL_DAMAGE_HYDRO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.HYDRO.value
    )
    ELEMENTAL_DAMAGE_GEO = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.GEO.value
    )
    ELEMENTAL_DAMAGE_PHYS = localization_enum.Artifacts.PercentStat.ELEMENTAL_DAMAGE.value.format(
        localization_enum.Artifacts.Elements.PHYS.value
    )


class ArtifactSet(enum.StrEnum):
    GLADIATORS_FINALE = localization_enum.Artifacts.ArtifactSet.GLADIATORS_FINALE.value
    WANDERERS_TROUPE = localization_enum.Artifacts.ArtifactSet.WANDERERS_TROUPE.value
    NOBLESSE_OBLIGE = localization_enum.Artifacts.ArtifactSet.NOBLESSE_OBLIGE.value
    BLOODSTAINED_CHIVALRY = localization_enum.Artifacts.ArtifactSet.BLOODSTAINED_CHIVALRY.value
    MAIDEN_BELOVED = localization_enum.Artifacts.ArtifactSet.MAIDEN_BELOVED.value
    VIRIDESCENT_VENERER = localization_enum.Artifacts.ArtifactSet.VIRIDESCENT_VENERER.value
