from pydantic import BaseModel
from typing import Literal


class Flight(BaseModel):
    OPERA: Literal['American Airlines', 'Air Canada', 'Air France', 'Aeromexico',
                    'Aerolineas Argentinas', 'Austral', 'Avianca', 'Alitalia',
                    'British Airways', 'Copa Air', 'Delta Air', 'Gol Trans', 'Iberia',
                    'K.L.M.', 'Qantas Airways', 'United Airlines', 'Grupo LATAM',
                    'Sky Airline', 'Latin American Wings', 'Plus Ultra Lineas Aereas',
                    'JetSmart SPA', 'Oceanair Linhas Aereas', 'Lacsa']
    TIPOVUELO: Literal['I', 'N']
    MES: Literal[tuple(range(1,12))]