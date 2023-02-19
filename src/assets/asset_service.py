from src.assets.assert_repo import asset_data_repo, asset_repo
from src.assets.models import Asset, AssetData

from . import schemas


class AssetService:
    def __init__(self) -> None:
        self.repo = asset_repo
        self.data_repo = asset_data_repo

    def create_assert(self, asset_data: schemas.AssetCreate):
        pass
