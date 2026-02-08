from typing import Type

from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

from artifacts.models import Artifact, ArtifactSubStat
from bot.media.media import EnkaArtifactImageProvider
from bot.models import ColorsEnums
from bot.settings import BotSettings
from localization.localization_data import BaseLocalization
from localization.interface import Localization

settings = BotSettings()

localization: Type[BaseLocalization] = Localization.get_localization()


def draw_text_with_fit(draw_obj, text, position, max_width, font_path, initial_font_size, fill):
    font_size = initial_font_size
    font = ImageFont.truetype(font_path, font_size)

    while True:
        bbox = draw_obj.textbbox((position[0], position[1]), text, font=font)
        text_width = bbox[2] - bbox[0]

        if text_width <= max_width or font_size <= 5:
            break

        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw_obj.textbbox((position[0], position[1]), text, font=font)
    text_height = text_bbox[3] - text_bbox[1]

    vertical_offset = (text_height // 2)
    adjusted_position = (position[0], position[1] - vertical_offset)

    draw_obj.text(adjusted_position, text, font=font, fill=fill)


class ArtifactImageGenerator:
    @staticmethod
    def get_artifact_main_stat_value_str(artifact: Artifact) -> str:
        if artifact.main_stat.is_percent:
            string_value = f"{round(artifact.main_stat.value, 1)}%"
        else:
            string_value = (f"{int(artifact.main_stat.value):,}"
                            .replace(",",
                                     localization.Artifacts.ARTIFACT_MAIN_STAT_DELIMITER))

        return string_value

    @staticmethod
    def get_substat_value_str(substat: ArtifactSubStat) -> str:
        base = f"{substat.stat.value}{localization.Artifacts.ARTIFACT_SUBSTAT_DELIMITER}+"
        if substat.is_percent:
            value = f"{round(substat.value, 1)}%"
        else:
            value = f"{round(substat.value)}"

        return base + value

    @classmethod
    async def generate_artifact_image(
            cls,
            artifact: Artifact
    ) -> bytes:
        background_image = Image.open(f'{settings.static_folder}/src/background.png')

        artifact_image = await EnkaArtifactImageProvider.get_artifact_image(
            artifact_set=artifact.set,
            artifact_type=artifact.type,
        )
        artifact_image.resize((160, 160))

        draw_obj = ImageDraw.Draw(background_image)
        font = f"{settings.static_folder}/src/fonts/gi_font.ttf"

        draw_obj.text(  # rendering level
            (40, 231),
            f'+{artifact.level}',
            fill=ColorsEnums.ARTIFACT_LEVEL.value,
            font=ImageFont.truetype(font, 17),
            anchor='mm'
        )

        for i, substat in enumerate(artifact.sub_stats):  # rendering substats
            position = (24, 256 + (i * 25))
            text = cls.get_substat_value_str(substat)
            substat_font = ImageFont.truetype(font, 17)

            if substat.is_active:
                color = ColorsEnums.SUBSTAT_ACTIVE.value
            else:
                text += f"\n({localization.Artifacts.ARTIFACT_INACTIVE_SUBSTAT})"
                color = ColorsEnums.SUBSTAT_NOT_ACTIVE.value

            draw_obj.text(
                position,
                "\u00B7",
                fill=color,
                font=substat_font
            )

            draw_obj.text(
                (position[0] + 15, position[1]),
                text,
                fill=color,
                font=substat_font
            )

        draw_obj.text(  # rendering artifact main stat name
            (20, 113),
            artifact.main_stat.stat.value,
            fill=ColorsEnums.MAIN_STAT_NAME.value,
            font=ImageFont.truetype(font, 15)
        )
        draw_obj.text(  # rendering main stat value
            (18, 130),
            cls.get_artifact_main_stat_value_str(artifact),
            fill=ColorsEnums.MAIN_STAT_VALUE.value,
            font=ImageFont.truetype(font, 30)
        )

        background_image.paste(artifact_image, (175, 30), mask=artifact_image)  # rendering artifact image
        draw_text_with_fit(  # rendering artifact name
            draw_obj=draw_obj,
            text=artifact.name,
            position=(22, 18),
            max_width=320,
            font_path=font,
            initial_font_size=20,
            fill=ColorsEnums.ARTIFACT_NAME.value
        )
        draw_obj.text(  # rendering artifact type name
            (22, 50),
            artifact.type.value,
            fill=ColorsEnums.ARTIFACT_TYPE_NAME.value,
            font=ImageFont.truetype(font, 15)
        )

        byte_io = BytesIO()
        background_image.save(byte_io, format='PNG')
        byte_io.seek(0)

        return byte_io.getvalue()
