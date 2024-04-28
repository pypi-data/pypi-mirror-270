import requests
import json

info = {
    "version": "0.1",
    "author": "ShawnMerry",
    "buildTime": "2404270236"
}


def login(identity, password):
    response = requests.post("https://api.codemao.cn/tiger/v3/web/accounts/login",
                             json={"pid": "65edCTyg", "identity": identity, "password": password})
    return {"status": response.status_code, "data": json.loads(response.text)}


def logout():
    response = requests.post("https://api.codemao.cn/tiger/v3/web/accounts/logout")
    return {"status": response.status_code}


def user_info(mode, datas=None, token=None):
    if mode == 0:  # change info
        response = requests.patch("https://api.codemao.cn/tiger/v3/web/accounts/info",
                                  json=datas, cookies={"authorization": token})
        return {"status": response.status_code}
    elif mode == 1:  # info
        response = requests.get("https://api.codemao.cn/api/user/info",
                                cookies={"authorization": token})
        return {"status": response.status_code, "data": json.loads(response.text)}
    elif mode == 2:  # details
        response = requests.get("https://api.codemao.cn/web/users/details",
                                cookies={"authorization": token})
        return {"status": response.status_code, "data": json.loads(response.text)}
    elif mode == 3:  # other's info
        response = requests.get("https://api.codemao.cn/api/user/info/detail/" + datas["user_id"])
        return {"status": response.status_code, "data": json.loads(response.text)}
    else:
        return {"status": 0}


def like(mode, like_id, token):
    if mode == 0:  # Work's like
        response = requests.post("https://api.codemao.cn/nemo/v2/works/" + like_id + "/like",
                                 cookies={"authorization": token})
        return {"status": response.status_code}
    elif mode == 1:  # Comment's like
        response = requests.put("https://api.codemao.cn/web/forums/comments/" + like_id + "/liked?source=REPLY",
                                cookies={"authorization": token})
        return {"status": response.status_code}
    else:
        return {"status": 0}


def collection(work_id, token):
    response = requests.post("https://api.codemao.cn/nemo/v2/works/" + work_id + "/collection",
                             cookies={"authorization": token})
    return {"status": response.status_code}


def fork(work_id, token):
    response = requests.post("https://api.codemao.cn/nemo/v2/works/" + work_id + "/fork",
                             cookies={"authorization": token})
    return {"status": response.status_code}


def follow(user_id, token):
    response = requests.post("https://api.codemao.cn/nemo/v2/user/" + user_id + "/follow",
                             cookies={"authorization": token})
    return {"status": response.status_code}


def report(mode, description, report_id, reason_content, token):
    if mode == 0:  # Post report
        response = requests.post("https://api.codemao.cn/web/reports/posts",
                                 json={"description": description, "post_id": report_id, "reason_id": reason_content},
                                 cookies={"authorization": token})
        return {"status": response.status_code}
    elif mode == 1:  # Work report
        response = requests.post("https://api.codemao.cn/nemo/v2/report/work",
                                 json={
                                     "work_id": report_id,
                                     "report_reason": reason_content,
                                     "report_describe": description
                                 }, cookies={"authorization": token})
        return {"status": response.status_code}
    else:
        return {"status": 0}
