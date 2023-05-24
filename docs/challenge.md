
# LATAM challenge - María José Apolo


## Implementation

### Part I
#### Fixes

Before operationalized the model, It was necessary to execute some fixes. The following table shows a summary of the main fixes. 


| File |Fixes |
| --- | --- | 
| `utils.py` | * get_period_day had extra intervals - * get_rate_from_column antipattern iterrows fix - * Delay rate formula correction rate = delay<class> / total<class> | 
| `model.py` | * Union parenthesis correction |
| `Makefile` | * Test was repeated and therefore, overwritten. - * Stress_test path folder correction| 
| `test_model.py` | * Test_model_fit was computing .fit function over the whole dataset, then computing predict over already seen data| 
| `requirements.txt` | * XGBoost added | 

#### Variables

The following table shows the candidate training attributes, its preprocessing options and extra details.

| Attribute | Type | Preprocessing | Extra |
| --- | --- | --- | --- |
| `DIA/MES` | Categorical Ordinal / Cyclic variables | Onehot encoding / SinCos representation| MES was finally choosen due to notable influence based on plots information|
| `DIANOM` | Categorical Ordinal / Cyclic variable | Categorical Ordinal / Cyclic variable | This variable didn't show impact in performance |
| `AÑO` | Numerical variable | Normalization | This variable didn't show significative impact in performance |
| `TIPO_VUELO` | Categorical Nominal | Onehot Encoding| Selected attribute based on notable importance show in plots|
| `OPERA` | Categorical Nominal | Onehot Encoding| Selected attribute based on notable importance show in plots information|
| `SIGLADES` | Categorical Nominal HIGH DIMENSIONALITY | Select top k values based on distribution, replace the remaining ones with 'Other' | Including this variable showed notable decreased in performance even after preprocessing|
| `SIGLAORI`| Categorical Nominal | One hot encoding | All flights took off from 'Santiago' |
| `high_season`| Categorical Binary | Numeric | This variable didn't show significative impact in performance |
| `period_day`| Categorical Ordinal / Cyclic variable | Categorical Ordinal / Cyclic variable | This variable didn't show impact in performance |


#### Hyperparameters tuning

* XGBoost: 
  - max_depth: maximum depth of a tree. values = [3,4,5,6,7]
  - min child weight: minimum sum of weights of all observations required in the child [1,2,3]

  Best parameters: max_depth: 5, min_child_weight: 1, recall: 0.72

* Logistic Regression 
  - solver. values = ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
  - penalty: regularization. ['none', 'l1', 'l2', 'elasticnet']
  - C [100,10,1,0.1,0.01]

  Best parameters: Hyperparameter tuning didn't show further improvement.

#### Model Comparison

*XGBoost: ML Opensource library which contains and optimal implementation of Gradient Boosting Algorithm Based on Trees. 
*Logistic Regression: Curvy linearly approach that analized the dependencies between a set of variables. 

Option: XGBoost

Reasoning: 
 
* Logistic Regression is an ideal model to tackle problems in which there is a linear relationship between variables. On the other hand, XGBoost can represent decision rules of greater complexity that would be more suitable considering the observed behavior of the training attributes.

* Additionally, given the high dimensionality of the classes present in the input variables, we are faced with a high-dimensional dataset where it is necessary to employ strategies such as prioritizing the most important variables. Given this complexity, it is my belief that XGBoost has greater potential to tackle this problem, given its robustness in handling the overfitting that can occur in high-dimensional datasets with a limited number of rows.

* Furthermore, it is of utmost importance to consider that this is a clear case of class imbalance with a 4:1 ratio, for which it has been shown that tree-based models are more robust to this type of problem.

* Despite the results obtained for both models in their default versions, XGBoost is notably superior to Logistic Regression in terms of the potential it can achieve through hyperparameters tuning. This is demonstrated both in the number of adjustable parameters that XGBoost has compared to the limited number of Logistic Regression, as well as in the competitive benchmark results obtained with this model. This gives XGBoost greater potential for future improvements in this implementation.

* On the other hand, the computational efficiency of XGBoost makes it a relevant candidate when it comes to deploying a cloud service, where latency and stress tests are important parameters to evaluate.

* Finally, XGBoost also offers explicability in order to understand the rules which commandate its decision making and make it more easily understandable. 

#### Good programming practices

There is significant place for improvement in my approach. One practical example, add a configuration file for paths or dictionaries. Feedback in this topic would be appreciated!

#### Test Model

In order to execute test-model, the following commands have to be executed:

```make venv
source .venv/bin/activate
make install
make test-model
```
The result shows 4/4 test completion [with warning!].

## Part II

#### Run server

To run the test, you need to compile and execute the Dockerfile to deploy the API locally, and then perform the tests towards the API. The commands to execute the Dockerfile are as follows:

```docker build -t gcr.io/prueba-latam-challenge/myapp .
docker run -dp 1243:1243 -e PORT=1243 gcr.io/prueba-latam-challenge/myapp
```

### Execute test
Once the API is running on localhost:1243, it's time to start the testing:

```source .venv/bin/activate
make api-test
```

Test results showed 4/4 completion [with warnings].

Considerations: 

* json format was modified in order to enhance a more simple and easy structure.
* The error code 400 has been replaced with the error code 422 because this error provides more information. Additionally, considering the validation performed with typing, it is capable of identifying the erroneous parameter and providing valid values.


## Part III

#### Deployment

Finally, the service was deployed on Google Cloud. It is actually running on: 

```
https://mjapp-mwpwxnmowa-uc.a.run.app/
```

In order to execute the stress-test, the following command have to be executed:

```
source .venv/bin/activate
make stress-test
```
