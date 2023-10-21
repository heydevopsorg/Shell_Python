import requests

def test_api_get():
    resp = requests.get("https://reqres.in/api/users?page=2")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 7:
            if record['first_name'] == "Michael":
                print("Data matched!")


def test_api_post():
    data = {'name': 'PRIME',
            'job': 'DEVOPS'}
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    data = resp.json()
    print(data)
    

test_api_get()

test_api_post()
