import requests
import names
from selenium import webdriver

### 1
def test_github(threshold):
    github_api = requests.get("https://api.github.com/users/avielb/repos")
    repo_list = github_api.json()
    assert len(repo_list) > threshold


### 2
def test_name_age():
    for i in range(3):
        name = names.get_first_name()
        age = requests.get(f"https://api.agify.io/?name={name}").json()
        assert age["age"] in range(1,120), f"{name}'s age is not between 1-120"


### 3
def test_isreal_universities(threshold):
    assert len(requests.get("http://universities.hipolabs.com/search?country=Israel").json()) > threshold


### 4 + 5
def test_selenium_title(url,title):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    assert my_driver.title == title, f"{url}'s title is not {title}"


# 1
test_github(5)

# 2
test_name_age()

# 3
test_isreal_universities(5)

# 4 + 5
dict = {"https://www.ycombinator.com/":"Y Combinator",
          "https://hub.docker.com":"Docker Hub Container Image Library | App Containerization"}

for i in dict.keys():
    test_selenium_title(i, dict[i])