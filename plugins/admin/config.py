from pydantic import BaseModel, validator
from aiosqlite import  Connection


class Config(BaseModel):
    admin: None

class Scoped(BaseModel):
    conn: Connection

    @validator("conn")
    async def conn_validator(cls, path):
        pass