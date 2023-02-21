from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


# Abstraction
class AbstractModel(BaseModel):
    class Config:
        use_enum_values = True
        orm_mode = True


class ResponseModel(AbstractModel):
    message: str
    status: int


# Asset  classes
class AssetCreate(AbstractModel):
    title: str


class AssetResponse(AbstractModel):
    id: int
    title: str
    date_added: datetime


class MessageAssetResp(ResponseModel):
    data: AssetResponse


class MessageListAssetResp(ResponseModel):
    data: List[AssetResponse]


# AsserData from integration API


class AssetDataResp(AbstractModel):
    id: int
    asset: AssetResponse
    price: float
    price_change: float
    funding_rate: float
    open_interest: float
    volume: float
    marketcap_ratio: Optional[float]
    date_added: datetime


class MessageListDataResp(ResponseModel):
    data: List[AssetDataResp]
