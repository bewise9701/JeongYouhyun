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

#keyword = input("What do you looking for?")

def count_page(keyword):
    base_url = "https://www.saramin.co.kr/zf_user/search?searchType=search&searchword="
    browser.get(f"{base_url}{keyword}&recruitPage=")

    #해당 창에서는 바로 원하는 코드를 찾을 수 없었으며, 임의로 버튼을 눌러서 페이지에 들어가야함.
    #더 보기 버튼을 눌러주는 코드를 작성하였음.
    buttons = browser.find_elements(By.CSS_SELECTOR, 'a[target="recruit_more"]')
    if len(buttons) == 0 :
        print("found 1 page")
        page_html = browser.page_source
        soup = BeautifulSoup(page_html, "html.parser")
    else:
        buttons[0].click()
        browser.implicitly_wait(3)
        #더보기 버튼을 클릭한 후의 페이지를 불러오게 하였음. 만약 불러오기 버튼이
        page_source = browser.page_source
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # 클릭된 화면에서 페이지 수 추출하기
        pagination = soup.find("div", class_="content_bottom")
        page_links = pagination.find_all("span")
        page_count = len(page_links)
        page_counter = 1
        page_buttons = pagination.select('a[data_track_event="total_search|"]')

        # 만약 페이지의 수가 10개인 경우와 그보다 작은 경우로 나눠 페이지의 개수를 출력하게 함.
        # 그리고 각각의 페이지를의 코드를 모두 다 불러오게 하고 수를 메겨 작동하는지 확인하기.
        if page_count < 10:
            print(f"found {page_count} pages")
            page_html = browser.page_source
            soup = BeautifulSoup(page_html, "html.parser")
            # 각 페이지에 넘버링(page_counter를 이용함.)
            print(f"Page : {page_counter}")
            # 각 페이지의 버튼을 클릭하기
            for i in range(1, page_count + 1):
                page_buttons = pagination.select('a[data_track_event="total_search|"]')
                if i > 1:
                    page_buttons = pagination.select('a[data_track_event="total_search|"]')
                    if page_buttons:
                        page_buttons[-1].click()
                    else:
                        print("Last page.")
                        break
                browser.implicitly_wait(1)
                for page_button in page_buttons:
                    if not page_button.is_enabled():
                        print(f"{page_button} is unavailable.")
                        print("0")
                    else:
                        print("1")

                # 페이지 소스 및 파싱
                page_html = browser.page_source
                soup = BeautifulSoup(page_html, "html.parser")

                # 페이지 카운터 변수 증가 및 페이지 출력
                page_counter += 1
                print(f"Page {page_counter}:")

        elif page_count == 10:
            print("found 10 pages")

            for page_button in page_buttons:
                if not page_button.is_enabled():
                    print("none, ", page_button)
                    print("0")
                else:
                    print("1")


'''
아직 완벽한 추출기로서의 기능은 아니나 페이지를 출력하는데에는 문제가 없음.
이후에 해결해야하는 문제가 count page 함수와 extractor을 결합하고, 10장 이상의 페이지일 때 모든 장이 출력되도록 하는 것이 목표임(안된다면 다른걸로 도전한 후 추가할 예정임.)
큰 두단계를 넘었고, 마지막 단계만 한다면 마무리 할 수 있을거 같다.
그리고 이제 다른 활동으로 인해서 시간이 좀 부족한데 더 노력하면서 공부하면 할 수 있다고 생각한다. 열심히 하자!
'''
