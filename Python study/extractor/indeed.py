from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#selenium을 이용하여 브라우저에 접속
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

#추출하는 자료는 한 페이지가 아니라 여러 장에 걸쳐서 있기 때문에 추가적인 코드를 작성해 주어야 한다.
def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # 강의에서는 ul -> li로 구성이 되었으나 시간이 지나 코드가 수정되어 nav -> div 변경됨.
    pagination = soup.find("nav", role = "navigation")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    #page의 수가 5 이상이면 5로 출력하고, 나머지는 페이지 수를 써준다.
    count = len(pages)
    if count >= 5 :
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    #위에 함수에서 page 개수를 받아서 넘겨줌.
    print("Found ", pages, " pages")
    results = []
    for page in range(pages):
        #페이지의 url이 10의 단위로 증가하기에(0, 10, 20, ...) 이를 적용하여 모든 자료를 추출하도록 한다.
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting ", final_url)
        browser.get(final_url)
        #beautifulsoup를 이용하여 웹페이지 소스코드 가져옴.
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        #job list안에 수많은 li가 있으나 우리는 ul 다음에 있는 것만 찾기를 원한다. 그래서 recursive를 이용함.
        jobs = job_list.find_all('li', recursive = False)
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            #1차적으로 거른 후에도 다른 것들이 섞여 있기 때문에 None(False와 다름, 아예 없음을 뜻함)을 이용하여 다시 걸러낸다.
            if zone == None:
                #select는 css selector 를 사용한다. 이를 사용하여 h2 안의 a 태그를 찾아준다.
                anchor = job.select_one("h2 a")
                # 기존 코드에서 수정한 부분으로 h2 에 aria-label 이 없는 부분이 있어서 오류가 발생하는 걸 막아줌.
                if anchor != None:
                    #wwr 스크래퍼와 마찬가지로 dict 안에 소스를 추출해줌
                    title = anchor['aria-label']
                    link = anchor['href']
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        'position': title.replace("의 전체 세부 정보", "").replace(",", " "),
                        'link': f"https://kr.indeed.com{link}",
                        'company': company.string.replace(",", " "),
                        'location' : location.string.replace(",", " ")
                    }
                    results.append(job_data)
    return results
