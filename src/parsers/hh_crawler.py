import requests
from bs4 import BeautifulSoup
import fake_useragent
import time

def get_links(text):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=f'https://hh.ru/search/vacancy?text={text}&area=1',
        headers={"user-agent": ua.random}
    )
    if data.status_code != 200:
        return
    soup = BeautifulSoup(data.content, "lxml")
    try:
        page_count = int(soup.find("div", attrs={"class":"pager"}).find_all("span", recursive=False)[-1].find("a", attrs={"class":"bloko-button"}).find("span").text)
    except:
        return
    for page in range(page_count):
        try:            
            data = requests.get(
                url=f'https://hh.ru/search/vacancy?text={text}&area=1&page={page}',
                headers={"user-agent": ua.random}
            )
            if data.status_code == 200:
                soup = BeautifulSoup(data.content, "lxml")
                for a in soup.find_all("a", attrs={"class":"serp-item__title"}):
                    yield f"{a.attrs['href'].split('?')[0]}"
        except Exception as ex:
            print(f"Error: {ex}")
        time.sleep(1)
    print(page_count)

def get_vacancy(link):
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url=link,
        headers={"user-agent":ua.random}
    )
    if data.status_code == 200:
        soup = BeautifulSoup(data.content, "lxml")
        try:
            name = soup.find("div", attrs={"class":"vacancy-title"}).find("h1").text.replace(u'\xa0', u' ')
        except:
            name = ""
        try:
            salary = soup.find("div", attrs={"class":"vacancy-title"}).find("div", attrs={"data-qa":"vacancy-salary"}).text.replace(u'\xa0', u'')
        except:
            salary = ""
        try:
            company_name = soup.find("span", attrs={"class":"vacancy-company-name"}).text.replace(u'\xa0', u' ')
        except:
            company_name = ""
        try:
            if bool(soup.find("p", attrs={"data-qa":"vacancy-view-location"})) == True:
                location = soup.find("p", attrs={"data-qa":"vacancy-view-location"}).text.replace(u'\xa0', u' ')
            else:
                location = soup.find("a", attrs={"class":"bloko-link bloko-link_kind-tertiary bloko-link_disable-visited"}).text.replace(u'\xa0', u' ')
        except:
            location = ""
        vacancy = {
            "name": name,
            "company_name": company_name,
            "salary": salary,
            "location": location,
            "reference": link
        }
        return vacancy

if __name__ == "__main__":
    for a in get_links("python"):
        print(get_vacancy(a))
        time.sleep(1)