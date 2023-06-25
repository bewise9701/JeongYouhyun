from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#selenium을 이용하여 브라우저에 접속
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

base_url = "https://www.saramin.co.kr/zf_user/search?searchType=search&searchword="
browser.get(f"{base_url}python")


def extract_saramin_jobs(keyword):
    results = []

    #추출하는 자료는 한 페이지가 아니라 여러 장에 걸쳐서 있기 때문에 추가적인 코드를 작성해 주어야 한다.
    base_url = "https://www.saramin.co.kr/zf_user/search?searchType=search&searchword="
    browser.get(f"{base_url}{keyword}&recruitPage=")

    #beautiful soup 사용해서 html 가져오기
    soup = BeautifulSoup(browser.page_source, "html.parser")
    items = soup.find_all('div', class_="item_recruit")
    for item in items:
        job_tit = item.find("h2", class_="job_tit")
        job_sector = item.find("div", class_="job_sector")
        job_corp = item.find("div", class_="area_corp")
        job_condition = item.find("div", class_="job_condition")
    #job_tit 영역에서 자료 추출하기
    # title과 link 추출하기
        title_anchor = job_tit.select_one("h2 a")
        if title_anchor is not None:
            title = title_anchor.get("title")
            link = title_anchor.get("href")

    # 직업의 sector(연관 분야) 추출하기
        anchor_sector_ba = job_sector.select_one("b a")
        anchor_sector_a = job_sector.select("a")
        if anchor_sector_a and anchor_sector_ba is not None:
            sector_raw = [a.get_text(strip=True) for a in anchor_sector_a]
            sector = ', '.join(sector_raw)

    # 직업의 위치, 채용 조건 추출하기
        anchor_condition = job_condition.find_all("span")
        condition_raw = [span.get_text(strip=True) for span in anchor_condition]
        condition = ', '.join(condition_raw)

    # 회사 명 추출하기
        corp_anchor = job_corp.find("a")
        corp = corp_anchor.get_text(strip=True)

    #추출한 정보들을 데이터로 정리하여 저장하기

        job_data = {
            'title' : title,
            'corp' : corp,
            'sector' : sector,
            'condition' : condition,
            'link' : f"https://www.saramin.co.kr{link}"
        }
        results.append(job_data)
    return results


