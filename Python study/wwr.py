from bs4 import BeautifulSoup
from requests import get

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?&term="
    response = get(f"{base_url}{keyword}")

    #html 불러오기(안불러지면 오류메세지 출력)
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        # BeautifulSoup를 이용하여 필요한 부분만 불러오기(section에서 jobs만 불러오기)
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_post = job_section.find_all('li')
            # li class에 딸려있는 view all 버튼 제거
            job_post.pop(-1)
            #jobs 안에 있는 job post만 불러오기
            for post in job_post:
                #job post 안에 href(링크)와 정보들 추출하여 저장하기
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                #자료 내에 다른 정보들이 company로 중복되어 있기에 구분해주기
                company, kind, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_="title")
                #추출된 정보들을 데이터로 정리하여 저장하기
                job_data = {
                    'position': title.string,
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string,
                    'location': region.string,
                }
                results.append(job_data)
    #결과값
    return results




