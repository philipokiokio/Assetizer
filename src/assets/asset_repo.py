# application imports
from src.app.utils.base_repo import BaseRepo
from src.assets.models import Asset, AssetData


# Asset Repository Abstraction of the DB calls
class AssetRepo(BaseRepo):
    @property
    def base_query(self):
        return self.db.query(Asset)

    def by_title(self, title: str):
        return self.base_query.filter(Asset.title.ilike(title)).first()

    def all_tracked_asset(self):
        return self.base_query.all()

    def by_id(self, id: int):
        return self.base_query.filter(Asset.id == id).first()

    def update(self, asset: Asset) -> Asset:
        self.db.commit()
        self.db.refresh(asset)
        return asset

    def create(self, asset_dict: dict) -> Asset:
        new_asset = Asset(**asset_dict)
        self.db.add(new_asset)
        self.db.commit()
        self.db.refresh(new_asset)
        return new_asset

    def delete(self, asset: Asset) -> None:
        self.db.delete(asset)
        self.db.commit()


# Abstracts AssetData DB calls
class AssetDataRepo(BaseRepo):
    @property
    def base_query(self):
        return self.db.query(AssetData)

    def create(self, asset_data: dict) -> AssetData:
        new_asset_data = AssetData(**asset_data)
        self.db.add(new_asset_data)
        self.db.commit()
        self.db.refresh(new_asset_data)
        return new_asset_data

    def get_by_asset(self, asset_id: int):
        return self.base_query.filter(AssetData.asset_id == asset_id).all()


# initalizing repos

asset_repo = AssetRepo()
asset_data_repo = AssetDataRepo()
