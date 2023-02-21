from celery import Celery
from celery.schedules import crontab

from src.app.utils._integration import asset_data_integrator
from src.assets.asset_repo import asset_data_repo, asset_repo

app = Celery("asset_job", broker="redis://localhost:6379/0")


@app.task
def asset_runner():
    # fetch all Assets and get data for the asset

    all_assets = asset_repo.all_tracked_asset()
    if all_assets:
        # for all the assets fetch data from CCTX and send to a Table
        for asset in all_assets:
            print(asset)
            asset_data = asset_data_integrator(asset.title)
            asset_data["asset_id"] = asset.id
            # saving data to a DB
            asset_data_repo.create(asset_data)
        return {"meessage": "Asset Data Retrieved and saved", "status": 200}
    return {"message": "No Asset in Assetizers, save and asset to start", "status": 404}


# Run the asset Job every 12 hours

app.add_periodic_task(
    crontab(minute=1),
    #   hour="*/12"),
    asset_runner.s(),
)
