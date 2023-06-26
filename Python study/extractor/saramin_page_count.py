from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from extractor.saramin import extract_saramin_jobs

#selenium을 이용하여 브라우저에 접속
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

base_url = "https://www.saramin.co.kr/zf_user/search?searchType=search&searchword="
browser.get(f"{base_url}아쿠아리스트&recruitPage=")

#해당 창에서는 바로 원하는 코드를 찾을 수 없었으며, 임의로 버튼을 눌러서 페이지에 들어가야함.
#더 보기 버튼을 눌러주는 코드를 작성하였음.
buttons = browser.find_elements(By.CSS_SELECTOR, 'a[target="recruit_more"]')
if len(buttons) == 0:
    print("found 1 page")

else:
    buttons.click()
    browser.implicitly_wait(5)
    #더보기 버튼을 클릭한 후의 페이지를 불러오게 하였음. 만약 불러오기 버튼이
    page_source = browser.page_source
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 클릭된 화면에서 페이지 수 추출하기
    pagination = soup.find("div", class_="content_bottom")
    page_links = pagination.find_all("span")
    page_count = len(page_links)

    if page_count <= 10:
        print(f"found {page_count} pages")
    else:
        print("found 10 pages")






