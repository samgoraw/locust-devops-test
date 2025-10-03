from locust import HttpUser, task, between

class MyStressTestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def sample_request(self):
        self.client.get("/posts")

    @task
    def create_post(self):
        self.client.post(
            "/posts",
            json={
                "title": "samtest",
                "body": "testbody",
                "userId": 1
            }
        )
