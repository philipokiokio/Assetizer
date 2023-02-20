from fastapi import HTTPException, status

from src.assets.asset_repo import asset_repo


def get_asset_dep(id: int):
    asset = asset_repo.by_id(id)

    if not asset:
        raise HTTPException(
            detail="Asset does not exist", status_code=status.HTTP_404_NOT_FOUND
        )
    return asset
