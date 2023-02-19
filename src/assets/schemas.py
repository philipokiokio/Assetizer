from typing import List, Optional

from pydantic import BaseModel, EmailStr


class AbstractModel(BaseModel):
    class config:
        use_enum_values = True

        orm_mode = True


class AssetCreate(AbstractModel):
    title: str
