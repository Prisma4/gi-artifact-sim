from io import BytesIO
from pathlib import Path
from PIL import Image
import httpx

from artifacts.constants import ArtifactType, ArtifactSet
from bot.media.models import ARTIFACT_TYPE_TO_ID, ARTIFACT_SET_TO_ID
from bot.settings import BotSettings

settings = BotSettings()
STATIC_DIR = Path(settings.static_folder)


class EnkaArtifactImageProvider:
    base_url: str = "https://enka.network/ui/"
    icon_template: str = "UI_RelicIcon_{}_{}.png"

    @classmethod
    async def get_artifact_image(
        cls,
        artifact_set: ArtifactSet,
        artifact_type: ArtifactType,
    ) -> Image.Image:
        try:
            set_id = ARTIFACT_SET_TO_ID[artifact_set]
            type_id = ARTIFACT_TYPE_TO_ID[artifact_type]
        except KeyError as e:
            raise ValueError(f"Mapping not found: {e}") from e

        local_dir = STATIC_DIR / "artifacts" / "sets" / str(set_id)
        local_dir.mkdir(parents=True, exist_ok=True)
        local_path = local_dir / f"{type_id}.png"

        if local_path.exists():
            return Image.open(local_path)

        url = cls.base_url + cls.icon_template.format(set_id, type_id)

        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            resp.raise_for_status()

        try:
            img = Image.open(BytesIO(resp.content))
            img.load()
        except Exception as e:
            raise ValueError(f"Downloaded file is not a valid image: {url}") from e

        img.save(local_path)
        return img
