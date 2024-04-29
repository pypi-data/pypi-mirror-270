import requests
import json

info = {
    "version": "0.1",
    "author": "ShawnMerry",
    "buildTime": "2404280016"
}


class login:
    def __init__(self, identity, password):
        response = requests.post("https://api.codemao.cn/tiger/v3/web/accounts/login",
                                 json={"pid": "65edCTyg", "identity": identity, "password": password})
        if response.status_code == 200:
            self.success = True
            self.token = json.loads(response.text)["auth"]["token"]
        else:
            self.success = False
        self.status = response.status_code
        self.data = json.loads(response.text)


class logout:
    def __init__(self):
        response = requests.post("https://api.codemao.cn/tiger/v3/web/accounts/logout")
        if response.status_code == 204:
            self.success = True
        else:
            self.success = False
        self.status = response.status_code


class user_info:
    def __init__(self, mode, datas=None, token=None):
        mode = int(mode)
        if mode == 0:  # change info
            response = requests.patch("https://api.codemao.cn/tiger/v3/web/accounts/info",
                                      json=datas, cookies={"authorization": token})
            if response.status_code == 204:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
        elif mode == 1:  # info
            response = requests.get("https://api.codemao.cn/api/user/info",
                                    cookies={"authorization": token})
            if response.status_code == 200:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
            self.data = json.loads(response.text)
        elif mode == 2:  # details
            response = requests.get("https://api.codemao.cn/web/users/details",
                                    cookies={"authorization": token})
            if response.status_code == 200:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
            self.data = json.loads(response.text)
        elif mode == 3:  # other's info
            response = requests.get("https://api.codemao.cn/api/user/info/detail/" + datas["user_id"])
            if response.status_code == 200:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
            self.data = json.loads(response.text)
        else:
            self.success = False
            self.status = 0


class like:
    def __init__(self, mode, like_id, token):
        mode = int(mode)
        like_id = str(like_id)
        if mode == 0:  # Work's like
            response = requests.post("https://api.codemao.cn/nemo/v2/works/" + like_id + "/like",
                                     cookies={"authorization": token})
            if response.status_code == 200:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
        elif mode == 1:  # Comment's like
            response = requests.put("https://api.codemao.cn/web/forums/comments/" + like_id + "/liked?source=REPLY",
                                    cookies={"authorization": token})
            if response.status_code == 204:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
        else:
            self.success = False
            self.status = 0


class collection:
    def __init__(self, work_id, token):
        work_id = str(work_id)
        response = requests.post("https://api.codemao.cn/nemo/v2/works/" + work_id + "/collection",
                                 cookies={"authorization": token})
        if response.status_code == 200:
            self.success = True
        else:
            self.success = False
        self.status = response.status_code


class fork:
    def __init__(self, work_id, token):
        work_id = str(work_id)
        response = requests.post("https://api.codemao.cn/nemo/v2/works/" + work_id + "/fork",
                                 cookies={"authorization": token})
        if response.status_code == 200:
            self.success = True
        else:
            self.success = False
        self.status = response.status_code


class follow:
    def __init__(self, user_id, token):
        user_id = str(user_id)
        response = requests.post("https://api.codemao.cn/nemo/v2/user/" + user_id + "/follow",
                                 cookies={"authorization": token})
        if response.status_code == 204:
            self.success = True
        else:
            self.success = False
        self.status = response.status_code


class report:
    def __init__(self, mode, description, report_id, reason_content, token):
        mode = int(mode)
        description = str(description)
        report_id = str(report_id)
        reason_content = str(reason_content)
        if mode == 0:  # Post report
            response = requests.post("https://api.codemao.cn/web/reports/posts",
                                     json={"description": description, "post_id": report_id,
                                           "reason_id": reason_content},
                                     cookies={"authorization": token})
            if response.status_code == 201:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
        elif mode == 1:  # Work report
            response = requests.post("https://api.codemao.cn/nemo/v2/report/work",
                                     json={
                                         "work_id": report_id,
                                         "report_reason": reason_content,
                                         "report_describe": description
                                     }, cookies={"authorization": token})
            if response.status_code == 200:
                self.success = True
            else:
                self.success = False
            self.status = response.status_code
        else:
            self.success = False
            self.status = 0
