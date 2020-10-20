import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2) # 1-2 seconds between simulatedevents

    @task # user task/behavior
    def index_page(self): 
        self.client.get("/")
        self.client.get("/")

    @task(3) # another user task 3 times more likely to happen
    def view_item(self):
        for item_id in range(10):
            self.client.get(f"/calc/sum?m={item_id}&n={42}", name="/calc/sum")
            time.sleep(1)

    def on_start(self): # init for each virtual user
        pass