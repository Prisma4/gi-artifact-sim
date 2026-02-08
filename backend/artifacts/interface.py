import random
from typing import List, Tuple, Dict, Type, Literal, Optional

from artifacts.constants import ArtifactType, Stat, PercentStat, ArtifactValueType, ArtifactSet
from artifacts.models import ArtifactSubStat, Artifact, ArtifactMainStat

from localization.localization_data import BaseLocalization
from localization.interface import Localization

localization: Type[BaseLocalization] = Localization.get_localization()


class ArtifactValueInterface:
    _possible_main_stats = {
        ArtifactType.FLOWER_OF_LIFE: [Stat.HP_FLAT, ],
        ArtifactType.PLUME_OF_DEATH: [Stat.ATK_FLAT, ],
        ArtifactType.SANDS_OF_EON: [
            PercentStat.ATK_PERCENT,
            PercentStat.DEFENCE_PERCENT,
            PercentStat.ENERGY_RECHARGE,
            Stat.ELEMENTAL_MASTERY,
            PercentStat.HP_PERCENT,
        ],
        ArtifactType.GOBLET_OF_EONOTHEM: [
            PercentStat.ATK_PERCENT,
            PercentStat.DEFENCE_PERCENT,
            Stat.ELEMENTAL_MASTERY,
            PercentStat.ELEMENTAL_DAMAGE_HYDRO,
            PercentStat.ELEMENTAL_DAMAGE_GEO,
            PercentStat.ELEMENTAL_DAMAGE_PYRO,
            PercentStat.ELEMENTAL_DAMAGE_PHYS,
            PercentStat.ELEMENTAL_DAMAGE_DENDRO,
            PercentStat.ELEMENTAL_DAMAGE_ANEMO,
            PercentStat.ELEMENTAL_DAMAGE_HYDRO,
            PercentStat.ELEMENTAL_DAMAGE_ELECTRO,
            PercentStat.HP_PERCENT,
        ],
        ArtifactType.CIRCLET_OF_LOGOS: [
            PercentStat.ATK_PERCENT,
            PercentStat.DEFENCE_PERCENT,
            Stat.ELEMENTAL_MASTERY,
            PercentStat.CRIT_DAMAGE,
            PercentStat.CRIT_RATE,
            PercentStat.HEAL_BONUS,
            PercentStat.HP_PERCENT,
        ],
    }
    _main_stat_values = {
        Stat.HP_FLAT: {
            ArtifactValueType.MIN: 717,
            ArtifactValueType.MAX: 4780,
        },
        Stat.ATK_FLAT: {
            ArtifactValueType.MIN: 47,
            ArtifactValueType.MAX: 311,
        },
        PercentStat.HP_PERCENT: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ATK_PERCENT: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.DEFENCE_PERCENT: {
            ArtifactValueType.MIN: 8.7,
            ArtifactValueType.MAX: 58.3,
        },
        Stat.ELEMENTAL_MASTERY: {
            ArtifactValueType.MIN: 28,
            ArtifactValueType.MAX: 186.5,
        },
        PercentStat.ENERGY_RECHARGE: {
            ArtifactValueType.MIN: 7.8,
            ArtifactValueType.MAX: 51.8,
        },
        PercentStat.ELEMENTAL_DAMAGE_PYRO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_CRYO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_ANEMO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_ELECTRO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_DENDRO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_HYDRO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_GEO: {
            ArtifactValueType.MIN: 7.0,
            ArtifactValueType.MAX: 46.6,
        },
        PercentStat.ELEMENTAL_DAMAGE_PHYS: {
            ArtifactValueType.MIN: 8.7,
            ArtifactValueType.MAX: 58.3,
        },
        PercentStat.CRIT_DAMAGE: {
            ArtifactValueType.MIN: 9.3,
            ArtifactValueType.MAX: 62.2,
        },
        PercentStat.CRIT_RATE: {
            ArtifactValueType.MIN: 4.7,
            ArtifactValueType.MAX: 31.1,
        },
        PercentStat.HEAL_BONUS: {
            ArtifactValueType.MIN: 5.4,
            ArtifactValueType.MAX: 35.9,
        },
    }
    _possible_sub_stats = {
        Stat.HP_FLAT,
        Stat.ATK_FLAT,
        Stat.DEFENCE_FLAT,
        Stat.ELEMENTAL_MASTERY,
        PercentStat.HP_PERCENT,
        PercentStat.ATK_PERCENT,
        PercentStat.DEFENCE_PERCENT,
        PercentStat.ENERGY_RECHARGE,
        PercentStat.CRIT_DAMAGE,
        PercentStat.CRIT_RATE,
    }
    _possible_substat_values = {
        Stat.HP_FLAT: [209.13, 239.00, 268.88, 298.75],
        Stat.ATK_FLAT: [13.62, 15.56, 17.51, 19.45],
        Stat.DEFENCE_FLAT: [16.20, 18.52, 20.83, 23.15],
        Stat.ELEMENTAL_MASTERY: [16.32, 18.65, 20.98, 23.31],
        PercentStat.HP_PERCENT: [4.08, 4.66, 5.25, 5.83],
        PercentStat.ATK_PERCENT: [4.08, 4.66, 5.25, 5.83],
        PercentStat.DEFENCE_PERCENT: [5.10, 5.83, 6.56, 7.29],
        PercentStat.ENERGY_RECHARGE: [4.53, 5.18, 5.83, 6.48],
        PercentStat.CRIT_DAMAGE: [5.44, 6.22, 6.99, 7.77],
        PercentStat.CRIT_RATE: [2.72, 3.11, 3.50, 3.89],
    }

    @classmethod
    def _get_sub_stats(
            cls,
            main_stat: Stat | PercentStat,
            forced: Optional[Stat | PercentStat] = None,
            substats_amount: int = 4
    ) -> List[Stat | PercentStat]:
        possible_stats = cls._possible_sub_stats.copy()
        if main_stat in possible_stats:
            possible_stats.remove(main_stat)

        if possible_stats and len(possible_stats) >= substats_amount:
            chosen_stats = []

            if forced is not None:
                if forced in possible_stats:
                    possible_stats.remove(forced)
                    chosen_stats.append(forced)
                    substats_amount -= 1

            for i in range(substats_amount):
                random_stat = random.choice(list(possible_stats))
                chosen_stats.append(random_stat)
                possible_stats.remove(random_stat)
            return chosen_stats

    @classmethod
    def get_substat_value(
            cls,
            substat: Stat | PercentStat,
            forced_value_luck: Optional[Literal[0, 1, 2, 3]] = None,
    ) -> float:
        possible_values = cls._possible_substat_values[substat]

        if forced_value_luck in [0, 1, 2, 3]:
            value = possible_values[forced_value_luck]
        else:
            value = random.choice(possible_values)

        return value

    @staticmethod
    def _count_main_stat(
            base_value: float,
            max_value: float,
            level: int = 0
    ) -> float:
        return base_value + (max_value - base_value) / 20 * level

    @classmethod
    def _get_substats_values(
            cls,
            substats: List[Stat | PercentStat],
            forced_luck: Optional[Literal[0, 1, 2, 3]] = None
    ) -> Dict[Stat | PercentStat, float]:
        substat_dict = {}

        for substat in substats:
            substat_dict[substat] = cls.get_substat_value(substat, forced_value_luck=forced_luck)

        return substat_dict

    @classmethod
    def _get_artifact_main_stat(
            cls,
            artifact_type: ArtifactType,
            forced_main_stat: Stat | PercentStat = None
    ) -> Stat | PercentStat:
        possible_values = cls._possible_main_stats[artifact_type]
        value = random.choice(possible_values)

        if forced_main_stat is not None:
            if forced_main_stat in possible_values:
                value = forced_main_stat

        return value

    @classmethod
    def get_artifact_main_stat_value(
            cls,
            main_stat: Stat | PercentStat,
            artifact_level: int = 0
    ) -> float:
        min_value = cls._main_stat_values[main_stat][ArtifactValueType.MIN]
        max_value = cls._main_stat_values[main_stat][ArtifactValueType.MAX]

        value = cls._count_main_stat(min_value, max_value, artifact_level)
        return value

    @classmethod
    def generate_artifact(
            cls,
            artifact_type: ArtifactType,
            forced_main_stat: Optional[Stat | PercentStat] = None,
            forced_sub_stat: Optional[Stat | PercentStat] = None,
            forced_substat_luck: Optional[Literal[0, 1, 2, 3]] = None
    ) -> Tuple[Stat | PercentStat, float, Dict[Stat | PercentStat, int | float]]:
        main_stat = cls._get_artifact_main_stat(artifact_type, forced_main_stat)
        main_stat_value = cls.get_artifact_main_stat_value(main_stat)

        random_substats = cls._get_sub_stats(main_stat=main_stat, forced=forced_sub_stat)
        substats = cls._get_substats_values(random_substats, forced_luck=forced_substat_luck)

        return main_stat, main_stat_value, substats


class ArtifactInterface:
    _artifact_names = localization.Artifacts.ARTIFACT_NAMES

    @classmethod
    def _get_artifact_name(
            cls,
            artifact_type: ArtifactType,
            artifact_set: ArtifactSet,
    ) -> str:
        return cls._artifact_names.get(artifact_set.value).get(artifact_type.value)

    @classmethod
    def generate_artifact_obj(
            cls,
            artifact_type: ArtifactType = ArtifactType.FLOWER_OF_LIFE,
            artifact_set: ArtifactSet = ArtifactSet.GLADIATORS_FINALE,
            forced_main_stat: Stat | PercentStat = None,
            forced_sub_stat: Stat | PercentStat = None,
            forced_sub_stat_luck: Optional[Literal[0, 1, 2, 3]] = None,
            force_fourth_stat: bool = False,
    ):
        main_stat, main_stat_value, substats = ArtifactValueInterface.generate_artifact(
            artifact_type=artifact_type,
            forced_main_stat=forced_main_stat,
            forced_sub_stat=forced_sub_stat,
            forced_substat_luck=forced_sub_stat_luck,
        )

        substat_objs = []

        is_fourth_stat_active = force_fourth_stat if force_fourth_stat else random.choice([True, False])

        substat_items = list(substats.items())

        for i, (substat, value) in enumerate(substat_items):
            is_last = i == len(substat_items) - 1

            substat_objs.append(
                ArtifactSubStat(
                    stat=substat,
                    value=value,
                    is_percent=isinstance(substat, PercentStat),
                    is_active=not (is_last and not is_fourth_stat_active),
                )
            )

        main_stat_obj: ArtifactMainStat = ArtifactMainStat(
            stat=main_stat,
            value=main_stat_value,
            is_percent=isinstance(main_stat, PercentStat),
        )

        artifact_obj: Artifact = Artifact(
            name=cls._get_artifact_name(artifact_type, artifact_set),
            type=artifact_type,
            main_stat=main_stat_obj,
            sub_stats=substat_objs,
            set=artifact_set,
        )

        return artifact_obj

    @classmethod
    def raise_artifact_level(
            cls,
            artifact: Artifact,
            forced_substat: Stat | PercentStat = None,
            forced_substat_luck: Optional[Literal[0, 1, 2, 3]] = None
    ) -> Tuple[ArtifactSubStat | None, float | None]:
        artifact.level += 1
        artifact.main_stat.value = ArtifactValueInterface.get_artifact_main_stat_value(artifact.main_stat.stat,
                                                                                       artifact.level)

        if artifact.level % 4 == 0:
            inactive_substats = [s for s in artifact.sub_stats if not s.is_active]

            if inactive_substats:
                substat_to_activate: ArtifactSubStat = random.choice(inactive_substats)
                substat_to_activate.is_active = True

                return substat_to_activate, substat_to_activate.value
            else:
                if forced_substat is not None:
                    matching_sub_stat = next(
                        (sub_stat for sub_stat in artifact.sub_stats if sub_stat.stat == forced_substat), None)
                    if matching_sub_stat is not None:
                        if forced_substat_luck in [0, 1, 2, 3]:
                            increase_value = ArtifactValueInterface.get_substat_value(forced_substat,
                                                                                      forced_substat_luck)
                        else:
                            increase_value = ArtifactValueInterface.get_substat_value(forced_substat)
                        matching_sub_stat.value += increase_value
                        return matching_sub_stat, increase_value

                chosen_substat: ArtifactSubStat = random.choice(artifact.sub_stats)
                increase_value = ArtifactValueInterface.get_substat_value(
                    substat=chosen_substat.stat,
                    forced_value_luck=forced_substat_luck
                )

                chosen_substat.value += increase_value

                return chosen_substat, increase_value

        return None, None
