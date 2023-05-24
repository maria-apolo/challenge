from locust import HttpUser, task

class StressUser(HttpUser):
    @task
    def predict_argentinas(self):
        self.client.post(
            "/predict", 
            json={
                        "OPERA": "Aerolineas Argentinas", 
                        "TIPOVUELO": "N", 
                        "MES": 3
            }
        )

    @task
    def predict_latam(self):
        self.client.post(
            "/predict", 
            json={

                        "OPERA": "Grupo LATAM", 
                        "TIPOVUELO": "N", 
                        "MES": 3
            }
        )