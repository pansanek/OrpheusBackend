from locust import HttpUser, TaskSet, task, between
from uuid import uuid4


class UserBehavior(TaskSet):
    def on_start(self):
        # This function is called when a simulated user starts.
        pass

    @task(1)
    def get_users(self):
        self.client.get("/api/users/")

    @task(2)
    def create_user(self):
        user_data = {
            "login": "testuser",
            "name": "Test User",
            "password": "password123",
            "email": "test@example.com",
            "about": "Test user description",
            "user_type": "regular",
            "profile_picture": {},
            "background_picture": {},
            "settings": {}
        }
        self.client.post("/api/users/", json=user_data)

    @task(1)
    def get_user_by_id(self):
        user_id = str(uuid4())
        self.client.get(f"/api/users/{user_id}")

    @task(1)
    def update_user(self):
        user_id = str(uuid4())
        user_data = {
            "login": "updateduser",
            "name": "Updated User",
            "password": "updatedpassword",
            "email": "updated@example.com",
            "about": "Updated user description",
            "user_type": "regular",
            "profile_picture": {},
            "background_picture": {},
            "settings": {}
        }
        self.client.put(f"/api/users/{user_id}", json=user_data)

    @task(1)
    def authorize_user(self):
        login = "testuser"
        password = "password123"
        self.client.get(f"/api/users/auth?login={login}&password={password}")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 9)  # Time between consecutive tasks
