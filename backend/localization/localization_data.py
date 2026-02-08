import enum


class AvailableLocalizations(enum.Enum):
    RU = "ru"
    EN = "en"


class BaseLocalization:
    class Keyboards:
        ROLL_ARTIFACTS = "Roll artifacts"
        CHANGE_ARTIFACT_SET = "Choose artifact set"
        CHANGE_ARTIFACT_TYPE = "Choose artifact type"

        SET_FORCED_MAINSTAT = "Choose forced main stat"
        SET_FORCED_SUBSTAT = "Choose forced substat"
        SET_FORCED_SUBSTAT_LUCK = "Choose forced substat luck"

        WORST_LUCK = "Worst luck"
        AVERAGE_LUCK = "Average luck"
        GOOD_LUCK = "Good luck"
        BEST_LUCK = "Best luck"

        NEW_ARTIFACT = "New artifact"
        LEVEL_UP_ARTIFACT = "Level up ( +4 )"

        PAGINATION_NEXT = "Next page"
        PAGINATION_PREVIOUS = "Previous page"

    class Messages:
        START_MESSAGE = "Welcome to the Artifact Simulator, {}! \nCreator - @Prisma4"
        ARTIFACT_CHOOSE_TYPE = "Choose artifact type:"
        ARTIFACT_CHOOSE_TYPE_SUCCESS = 'Artifact type successfully set to "{}"!'
        ARTIFACT_CHOOSE_SET = "Choose artifact set:"
        ARTIFACT_CHOOSE_SET_SUCCESS = 'Artifact set successfully set to "{}"!'
        SOMETHING_WENT_WRONG = "Something went wrong!"
        SOMETHING_WENT_WRONG_SPECIFIED = "Something went wrong: {}"
        ARTIFACT_NOT_FOUND = "Artifact not found!"
        ARTIFACT_SUBSTAT_WAS_INCREASED = "{} was increased by {}!"
        CHOOSE_FORCED_SUBSTAT = "Choose forced substat:"
        CHOOSE_FORCED_SUBSTAT_LUCK = "Choose forced substat luck:"
        CHOOSE_FORCED_MAINSTAT = "Choose forced main stat:"
        CHOOSE_FORCED_SUBSTAT_SUCCESS = "Forced substat successfully set to {}"
        CHOOSE_FORCED_SUBSTAT_LUCK_SUCCESS = "Forced substat luck successfully set to {}"
        CHOOSE_FORCED_MAINSTAT_SUCCESS = "Forced main stat successfully set to {}"

    class Artifacts:
        ARTIFACT_MAIN_STAT_DELIMITER = ","
        ARTIFACT_SUBSTAT_DELIMITER = ""
        ARTIFACT_INACTIVE_SUBSTAT = "Inactive"

        class ArtifactType:
            FLOWER_OF_LIFE = "Flower of life"
            PLUME_OF_DEATH = "Plume of death"
            SANDS_OF_EON = "Sands of eon"
            GOBLET_OF_EONOTHEM = "Goblet of eonothem"
            CIRCLET_OF_LOGOS = "Circle of logos"

        class Stat:
            HP_FLAT = "HP"
            ATK_FLAT = 'ATK'
            DEFENCE_FLAT = "DEF"
            ELEMENTAL_MASTERY = "Elemental Mastery"

        class Elements:
            PYRO = "Pyro"
            ANEMO = "Anemo"
            CRYO = "Cryo"
            ELECTRO = "Electro"
            DENDRO = "Dendro"
            HYDRO = "Hydro"
            GEO = "Geo"
            PHYS = "Phys"

        class PercentStat:
            HP_PERCENT = "HP"
            ATK_PERCENT = 'ATK'
            DEFENCE_PERCENT = "DEF"
            ENERGY_RECHARGE = "Energy Recharge"
            CRIT_DAMAGE = "Crit DMG"
            CRIT_RATE = "Crit Rate"
            HEAL_BONUS = "Heal Bonus"
            ELEMENTAL_DAMAGE = "{} DMG bonus"

        class ArtifactSet:
            GLADIATORS_FINALE = "Gladiator's Finale"
            WANDERERS_TROUPE = "Wanderer's Troupe"
            NOBLESSE_OBLIGE = "Noblesse Oblige"
            BLOODSTAINED_CHIVALRY = "Bloodstained Chivalry"
            MAIDEN_BELOVED = "Maiden Beloved"
            VIRIDESCENT_VENERER = "Viridescent Venerer"

        ARTIFACT_NAMES = {
            ArtifactSet.GLADIATORS_FINALE: {
                ArtifactType.FLOWER_OF_LIFE: "Gladiator's Nostalgia",
                ArtifactType.PLUME_OF_DEATH: "Gladiator's Destiny",
                ArtifactType.SANDS_OF_EON: "Gladiator's Longing",
                ArtifactType.GOBLET_OF_EONOTHEM: "Gladiator's Intoxication",
                ArtifactType.CIRCLET_OF_LOGOS: "Gladiator's Triumphus",
            },
            ArtifactSet.WANDERERS_TROUPE: {
                ArtifactType.FLOWER_OF_LIFE: "Troupe's Dawnlight",
                ArtifactType.PLUME_OF_DEATH: "Bard's Arrow Feather",
                ArtifactType.SANDS_OF_EON: "Concert's Final Hour",
                ArtifactType.GOBLET_OF_EONOTHEM: "Wanderer's String-Kettle",
                ArtifactType.CIRCLET_OF_LOGOS: "Conductor's Top Hat",
            },
            ArtifactSet.MAIDEN_BELOVED: {
                ArtifactType.FLOWER_OF_LIFE: "Maiden's Distant Love",
                ArtifactType.PLUME_OF_DEATH: "Maiden's Heart-Stricken Infatuation",
                ArtifactType.SANDS_OF_EON: "Maiden's Passing Youth",
                ArtifactType.GOBLET_OF_EONOTHEM: "Maiden's Fleeting Leisure",
                ArtifactType.CIRCLET_OF_LOGOS: "Maiden's Fading Beauty",
            },
            ArtifactSet.NOBLESSE_OBLIGE: {
                ArtifactType.FLOWER_OF_LIFE: "Royal Flora",
                ArtifactType.PLUME_OF_DEATH: "Royal Plume",
                ArtifactType.SANDS_OF_EON: "Royal Pocket Watch",
                ArtifactType.GOBLET_OF_EONOTHEM: "Royal Silver Urn",
                ArtifactType.CIRCLET_OF_LOGOS: "Royal Masque",
            },
            ArtifactSet.BLOODSTAINED_CHIVALRY: {
                ArtifactType.FLOWER_OF_LIFE: "Bloodstained Flower of Iron",
                ArtifactType.PLUME_OF_DEATH: "Bloodstained Black Plume",
                ArtifactType.SANDS_OF_EON: "Bloodstained Final Hour",
                ArtifactType.GOBLET_OF_EONOTHEM: "Bloodstained Chevalier's Goblet",
                ArtifactType.CIRCLET_OF_LOGOS: "Bloodstained Iron Mask",
            },
            ArtifactSet.VIRIDESCENT_VENERER: {
                ArtifactType.FLOWER_OF_LIFE: "In Remembrance of Viridescent Fields",
                ArtifactType.PLUME_OF_DEATH: "Viridescent Arrow Feather",
                ArtifactType.SANDS_OF_EON: "Viridescent Venerer's Determination",
                ArtifactType.GOBLET_OF_EONOTHEM: "Viridescent Venerer's Vessel",
                ArtifactType.CIRCLET_OF_LOGOS: "Viridescent Venerer's Diadem",
            },
        }


class RuLocalization(BaseLocalization):
    class Keyboards(BaseLocalization.Keyboards):
        ROLL_ARTIFACTS = "Крутить артефакты"
        CHANGE_ARTIFACT_SET = "Выбрать набор артефакта"
        CHANGE_ARTIFACT_TYPE = "Выбрать тип артефакта"

        SET_FORCED_MAINSTAT = "Выбрать обязательный главный стат"
        SET_FORCED_SUBSTAT = "Выбрать обязательный подстат"
        SET_FORCED_SUBSTAT_LUCK = "Выбрать обязательную удачу подстата"

        WORST_LUCK = "Худшая удача"
        AVERAGE_LUCK = "Средняя удача"
        GOOD_LUCK = "Нормальная удача"
        BEST_LUCK = "Лучшая удача"

        NEW_ARTIFACT = "Новый артефакт"
        LEVEL_UP_ARTIFACT = "Повысить уровень ( +4 )"

        PAGINATION_NEXT = "Следующая страница"
        PAGINATION_PREVIOUS = "Предыдущая страница"

    class Messages(BaseLocalization.Messages):
        START_MESSAGE = "Добро пожаловать в симулятор артефактов, {}! \nСоздатель бота - @Prisma4"
        ARTIFACT_CHOOSE_TYPE = "Выберите тип артефакта:"
        ARTIFACT_CHOOSE_TYPE_SUCCESS = 'Тип артефакта успешно установлен на "{}"!'
        ARTIFACT_CHOOSE_SET = "Выберите набор артефакта:"
        ARTIFACT_CHOOSE_SET_SUCCESS = 'Набор артефакта успешно установлен на "{}"!'
        SOMETHING_WENT_WRONG = "Что-то пошло не так!"
        SOMETHING_WENT_WRONG_SPECIFIED = "Что-то пошло не так: {}"
        ARTIFACT_NOT_FOUND = "Артефакт не найден!"
        ARTIFACT_SUBSTAT_WAS_INCREASED = "{} был повышен на {}!"
        CHOOSE_FORCED_SUBSTAT = "Выберите обязательный подстат:"
        CHOOSE_FORCED_SUBSTAT_LUCK = "Выберите обязательную удачу подстата:"
        CHOOSE_FORCED_MAINSTAT = "Выберите обязательный главный стат:"
        CHOOSE_FORCED_SUBSTAT_SUCCESS = "Обязательный подстат успешно установлен на {}"
        CHOOSE_FORCED_SUBSTAT_LUCK_SUCCESS = "Обязательная удача подстата успешно установлена на {}"
        CHOOSE_FORCED_MAINSTAT_SUCCESS = "Обязательный главный стат успешно установлен на {}"

    class Artifacts(BaseLocalization.Artifacts):
        ARTIFACT_MAIN_STAT_DELIMITER = " "
        ARTIFACT_SUBSTAT_DELIMITER = " "
        ARTIFACT_INACTIVE_SUBSTAT = "Неактивно"

        class ArtifactType(BaseLocalization.Artifacts.ArtifactType):
            FLOWER_OF_LIFE = "Цветок жизни"
            PLUME_OF_DEATH = "Перо смерти"
            SANDS_OF_EON = "Пески времени"
            GOBLET_OF_EONOTHEM = "Кубок пространства"
            CIRCLET_OF_LOGOS = "Корона разума"

        class Stat(BaseLocalization.Artifacts.Stat):
            HP_FLAT = "HP"
            ATK_FLAT = 'Сила атаки'
            DEFENCE_FLAT = "Защита"
            ELEMENTAL_MASTERY = "Мастерство стихий"

        class Elements(BaseLocalization.Artifacts.Elements):
            PYRO = "Пиро"
            ANEMO = "Анемо"
            CRYO = "Крио"
            ELECTRO = "Электро"
            DENDRO = "Дендро"
            HYDRO = "Гидро"
            GEO = "Гео"
            PHYS = "Физ"

        class PercentStat(BaseLocalization.Artifacts.PercentStat):
            HP_PERCENT = "HP"
            ATK_PERCENT = 'Сила атаки'
            DEFENCE_PERCENT = "Защита"
            ENERGY_RECHARGE = "Восст. энергии"
            CRIT_DAMAGE = "Крит. урон"
            CRIT_RATE = "Шанс крит. попадания"
            HEAL_BONUS = "Бонус лечения"
            ELEMENTAL_DAMAGE = "Бонус {} урона"

        class ArtifactSet(BaseLocalization.Artifacts.ArtifactSet):
            GLADIATORS_FINALE = "Конец гладиатора"
            WANDERERS_TROUPE = "Странствующий ансамбль"
            NOBLESSE_OBLIGE = "Церемония древней знати"
            BLOODSTAINED_CHIVALRY = "Рыцарь крови"
            MAIDEN_BELOVED = "Возлюбленная юная дева"
            VIRIDESCENT_VENERER = "Изумрудная тень"

        ARTIFACT_NAMES = {
            ArtifactSet.GLADIATORS_FINALE: {
                ArtifactType.FLOWER_OF_LIFE: "Ностальгия гладиатора",
                ArtifactType.PLUME_OF_DEATH: "Судьба гладиатора",
                ArtifactType.SANDS_OF_EON: "Стремление гладиатора",
                ArtifactType.GOBLET_OF_EONOTHEM: "Пьянство гладиатора",
                ArtifactType.CIRCLET_OF_LOGOS: "Триумф гладиатора",
            },
            ArtifactSet.WANDERERS_TROUPE: {
                ArtifactType.FLOWER_OF_LIFE: "Рассвет ансамбля",
                ArtifactType.PLUME_OF_DEATH: "Оперение стрелы барда",
                ArtifactType.SANDS_OF_EON: "Окончание концерта",
                ArtifactType.GOBLET_OF_EONOTHEM: "Фляжка странника",
                ArtifactType.CIRCLET_OF_LOGOS: "Цилиндр дирижёра",
            },
            ArtifactSet.MAIDEN_BELOVED: {
                ArtifactType.FLOWER_OF_LIFE: "Далёкая душа юной девы",
                ArtifactType.PLUME_OF_DEATH: "Тоска юной девы",
                ArtifactType.SANDS_OF_EON: "Уходящая молодость юной девы",
                ArtifactType.GOBLET_OF_EONOTHEM: "Досуг юной девы",
                ArtifactType.CIRCLET_OF_LOGOS: "Увядающая красота юной девы",
            },
            ArtifactSet.NOBLESSE_OBLIGE: {
                ArtifactType.FLOWER_OF_LIFE: "Королевский цветок",
                ArtifactType.PLUME_OF_DEATH: "Королевское перо",
                ArtifactType.SANDS_OF_EON: "Королевские карманные часы",
                ArtifactType.GOBLET_OF_EONOTHEM: "Королевская серебряная фляжка",
                ArtifactType.CIRCLET_OF_LOGOS: "Королевская маска",
            },
            ArtifactSet.BLOODSTAINED_CHIVALRY: {
                ArtifactType.FLOWER_OF_LIFE: "Железное сердце рыцаря крови",
                ArtifactType.PLUME_OF_DEATH: "Перо рыцаря крови",
                ArtifactType.SANDS_OF_EON: "Час долга рыцаря крови",
                ArtifactType.GOBLET_OF_EONOTHEM: "Кубок рыцаря крови",
                ArtifactType.CIRCLET_OF_LOGOS: "Железная маска рыцаря крови",
            },
            ArtifactSet.VIRIDESCENT_VENERER: {
                ArtifactType.FLOWER_OF_LIFE: "Воспоминания об изумрудных лугах",
                ArtifactType.PLUME_OF_DEATH: "Оперение стрелы изумрудного охотника",
                ArtifactType.SANDS_OF_EON: "Решимость изумрудного охотника",
                ArtifactType.GOBLET_OF_EONOTHEM: "Сосуд изумрудного охотника",
                ArtifactType.CIRCLET_OF_LOGOS: "Венок изумрудного охотника",
            },
        }


class EnLocalization(BaseLocalization):
    pass
