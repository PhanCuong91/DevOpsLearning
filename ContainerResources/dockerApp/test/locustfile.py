# python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1,3)

    @task
    def get_home(self):
        self.client.get("/")
