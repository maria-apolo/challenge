from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException 
import pandas as pd 

from Flight import Flight
from model import DelayModel

app = FastAPI()
delay_classifier = DelayModel()


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Predict Delay is running!'

@app.post('/predict')
def predict_delay(features: Flight):
    data = [features.OPERA, features.TIPOVUELO, features.MES]
    columns = ['OPERA', 'TIPOVUELO', 'MES']
    df = pd.DataFrame(columns=columns)
    df.loc[0] = data
    try:
        preprocessed_features = delay_classifier.preprocess(df)
    except:
        return HTTPException(status_code=400)
    pred = delay_classifier.predict(preprocessed_features)
    response_object = {
        "predict": pred.tolist()
    }
    return JSONResponse(response_object)