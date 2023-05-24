import pandas as pd
from challenge.utils import *
import xgboost as xgb
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

from typing import Tuple, Union, List

class DelayModel:

    def __init__(
        self,
        datafile =  './data/raw/data.csv'
    ):
        self._SAVE_PATH = './challenge/pretrained/' 
        self._model = None                  # Model should be saved in this attribute.                  
        self.data = pd.read_csv(datafile)

    def preprocess(
        self,
        data: pd.DataFrame,
        target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """

        top_10_features = [
            "OPERA_Latin American Wings", 
            "MES_7",
            "MES_10",
            "OPERA_Grupo LATAM",
            "MES_12",
            "TIPOVUELO_I",
            "MES_4",
            "MES_11",
            "OPERA_Sky Airline",
            "OPERA_Copa Air"
        ]


        encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
        nominal_encode = encoder.fit_transform(data[['OPERA','TIPOVUELO', 'MES']])
        if(target_column):

            data = add_derivated_features(data)
            #Converting back to a dataframe
            features_nominal = pd.DataFrame(nominal_encode, columns=encoder.get_feature_names_out())
            target = data[target_column].to_frame(name='delay')
            features = features_nominal[top_10_features]


            return (features,target)
        else:


            nominal_encode = encoder.transform(data[['OPERA','TIPOVUELO', 'MES']])
            features_nominal = pd.DataFrame(nominal_encode, columns=encoder.get_feature_names_out())
            features =pd.concat([features_nominal, 
                                pd.DataFrame(columns=top_10_features)
            ], axis=0)
            features = features[top_10_features].fillna(0)


            return features

    def fit(
        self,
        features: pd.DataFrame,
        target: pd.DataFrame
    ) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """

        n_y0 = len(target[target['delay'] == 0])
        n_y1 = len(target[target['delay'] == 1])
        scale = n_y0/n_y1

        self._model = xgb.XGBClassifier(random_state=1, learning_rate=0.01, scale_pos_weight = scale, max_depth=5, min_child_weight=1)
        self._model.fit(features, target['delay'])
        self._model.save_model(self._SAVE_PATH+"xgb_imp_weighted.json")
        return

    def predict(
        self,
        features: pd.DataFrame
    ) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.
        
        Returns:
            (List[int]): predicted targets.
        """

        self._model = xgb.XGBClassifier()
        self._model.load_model(self._SAVE_PATH+"xgb_imp_weighted.json")
        preds = self._model.predict(features)
        return preds.tolist()