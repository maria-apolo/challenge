from pydantic import BaseModel


class Flight(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int