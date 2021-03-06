from locust import HttpLocust, TaskSet, task
#web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        """
        on_start is called when a Locust start before any task is scheduled"""
    def login(self):
        self.client.post("/login_action",{"username":"admin","password":"admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("/event_manage/")
    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(1)
    def search_phone(self):
        self.client.get("/search_phone/",params={"phone":'13555555555'})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
