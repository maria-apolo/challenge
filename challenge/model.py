import pandas as pd
from utils import *
import xgboost as xgb
from sklearn.preprocessing import OneHotEncoder

from typing import Tuple, Union, List

class DelayModel:

    def __init__(
        self,
        datafile = '../data/raw/data.csv'
    ):
        self._model = None                  # Model should be saved in this attribute.
        self._ohe = None                    # ohe contains Onehot encoder for preds
        self._data = pd.read_csv(datafile)
        self._features, self._target = self.preprocess(data=self._data, target_column='delay')
        self.fit(self._features, self._target) 

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

 
        if(target_column):

            data = add_derivated_features(data)
            self._ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
            nominal_encode = self._ohe.fit_transform(data[['OPERA','TIPOVUELO', 'MES']])
            #Converting back to a dataframe
            features = pd.DataFrame(nominal_encode, columns=self._ohe.get_feature_names())
            target = data[target_column]
            return (features,target)
        else:
            nominal_encode = self._ohe.transform(data[['OPERA','TIPOVUELO', 'MES']])
            features = pd.DataFrame(nominal_encode, columns=self._ohe.get_feature_names())

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
        n_y0 = len(target[target == 0])
        n_y1 = len(target[target == 1])
        scale = n_y0/n_y1
        self._model = xgb.XGBClassifier(random_state=1, learning_rate=0.01, scale_pos_weight = scale, max_depth=5, min_child_weight=1)
        self._model.fit(features, target)
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
        preds = self._model.predict(features)
        return preds