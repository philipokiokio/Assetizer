# fastapi imports
from fastapi import HTTPException, status

# application import
from src.assets.asset_repo import asset_data_repo, asset_repo

from . import models, schemas


class AssetService:
    def __init__(self) -> None:
        self.repo = asset_repo
        self.data_repo = asset_data_repo

    def create_asset(self, asset_data: schemas.AssetCreate):
        # check if asset has been added for monitoring.

        asset_check = self.repo.by_title(asset_data.title)

        if asset_check:
            raise HTTPException(
                detail="Asset has been added and it is been tracked",
                status_code=status.HTTP_409_CONFLICT,
            )

        asset_data_dict = asset_data.dict()

        new_asset = self.repo.create(asset_data_dict)

        return {
            "message": "Asset created successfully",
            "data": new_asset,
            "status": status.HTTP_201_CREATED,
        }

    def get_all_assets(self):
        all_assets = self.repo.all_tracked_asset()

        if not all_assets:
            raise HTTPException(
                detail="No Asset has been added", status_code=status.HTTP_404_NOT_FOUND
            )

        return {
            "message": "All assets available",
            "status": status.HTTP_200_OK,
            "data": all_assets,
        }

    def get_asset(self, asset_id: int):
        asset = self.repo.by_id(asset_id)

        if not asset:
            raise HTTPException(
                detail="Asset does not exist", status_code=status.HTTP_404_NOT_FOUND
            )

        return {
            "message": "Asset retrieved successfully",
            "status": status.HTTP_200_OK,
            "data": asset,
        }

    def update_asset(self, asset_id: int, asset_update: schemas.AssetCreate):
        asset = self.repo.by_id(asset_id)

        if not asset:
            raise HTTPException(
                detail="Asset does not exist", status_code=status.HTTP_404_NOT_FOUND
            )

        for key, value in asset_update.dict().items():
            setattr(asset, key, value)

        asset = self.repo.update(asset)

        return {
            "message": "Asset updated successfully",
            "status": status.HTTP_200_OK,
            "data": asset,
        }

    def delete_asset(self, asset_id: int):
        asset = self.repo.by_id(asset_id)

        if not asset:
            raise HTTPException(
                detail="Asset does not exist", status_code=status.HTTP_404_NOT_FOUND
            )

        self.repo.delete(asset)

        return {
            "status": status.HTTP_204_NO_CONTENT,
        }

    def get_all_asset_data(self, asset_id: int):
        all_asset_data = self.data_repo.get_by_asset(asset_id)

        if not all_asset_data:
            raise HTTPException(
                detail="No Asset Data available", status_code=status.HTTP_404_NOT_FOUND
            )

        return {
            "message": "All asset data  available",
            "status": status.HTTP_200_OK,
            "data": all_asset_data,
        }


asset_service = AssetService()
