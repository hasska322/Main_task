import requests
from bs4 import BeautifulSoup as bs
import re
import lxml


def get_html(url):
    """
    function for getting page be requests
    : param url: URL for request
    : return : Page
    """
    #  Input your user - agent
    #  If wanna know your user-agent for Google command "about:"
    headers = {
        'User-Agent': ''
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'
    into_file(r.text)
    return r.text


def into_file(text):
    """"
    Save page into the file
    :param text: Page for saving
    """
    with open("target.html", "w", encoding="utf8") as target:
        print(text, file=target)


def soup_info(text):
    """Function for parsing title's of free video on Udemy
    : param text : Page for parsing
    :return file: Saved file with answer"""
    soup = bs(text, "lxml")
    head = soup.find("div", class_="lectures-container collapse in").find_all("a", href=re.compile("javascript"),
                                                                              class_=None)
    heads = [i.text for i in head if i.text != "\nPreview\n"]
    cleaner(heads)

    time = soup.find("div", class_='lectures-container collapse in').find_all("span", ["preview-text",
                                                                                       "content-summary"])
    times = [i.text for i in time]
    cleaner(times)

    i = 0
    while True:
        if times[i] == "Preview" or times[i] != "Preview" and times[i+1] == "Preview":
            i += 1
            continue
        elif times[i] != "Preview" and times[i+1] != "Preview":
            del times[i+1]
            i += 1
        if i >= len(times):
            break
    times = [i for i in times if i != "Preview"]
    answer = list(zip(heads, times))
    answer.sort(key=lambda i: i[1])
    with open("answer.txt", "w") as file:
        for i in answer:
            print(*i, file=file)


def cleaner(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
    return lst


udemy = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"

text_info = get_html(udemy)
into_file(text_info)
soup_info(text_info)
