from fastapi import APIRouter, Depends, status

from src.assets.models import Asset
from src.assets.pipe.asset_pipe import get_asset_dep

from . import schemas
from .asset_service import asset_service

asset_router = APIRouter(prefix="/v1/asset", tags=["Asset and Asset Tracked Data"])


@asset_router.post(
    "/create/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.MessageAssetResp,
)
def create_asset(asset_data: schemas.AssetCreate):
    resp = asset_service.create_asset(asset_data)
    return resp


@asset_router.get(
    "s/", status_code=status.HTTP_200_OK, response_model=schemas.MessageListAssetResp
)
def get_assets():
    resp = asset_service.get_all_assets()
    return resp


@asset_router.get(
    "/{id}/", status_code=status.HTTP_200_OK, response_model=schemas.MessageAssetResp
)
def get_asset(id: int):
    resp = asset_service.get_asset(id)
    return resp


@asset_router.patch(
    "/{id}/update/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageAssetResp,
)
def update_asset(id: int, asset_data: schemas.AssetCreate):
    resp = asset_service.update_asset(id, asset_data)
    return resp


@asset_router.delete("/{id}/delete", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset(id: int):
    resp = asset_service.delete_asset(id)
    return resp


@asset_router.get("/{id}/tracker/", status_code=status.HTTP_200_OK)
def track_asset(id: int, asset: Asset = Depends(get_asset_dep)):
    resp = asset_service.get_all_asset_data(asset.id)
    return resp
