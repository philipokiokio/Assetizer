from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from src.app.database import Base


class Asset(Base):
    __tablename__ = "Assets"
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    date_added = Column(
        TIMESTAMP(timezone=True),
        nullable=True,
        server_default=text("now()"),
    )


class AssetData(Base):
    __tablename__ = "Asset_Data"
    id = Column(Integer, nullable=False, primary_key=True)
    asset_id = Column(Integer, ForeignKey("Assets.id", ondelete="CASCADE"))
    price = Column(Float, nullable=True)
    price_change = Column(Float, nullable=True)
    funding_rate = Column(Float, nullable=True)
    open_interest = Column(Float, nullable=True)
    volume = Column(Float, nullable=True)
    marketcap_ratio = Column(Float, nullable=True)
    date_added = Column(
        TIMESTAMP(timezone=True),
        nullable=True,
        server_default=text("now()"),
    )
    asset = relationship("Asset")
