# 원본 = https://replit.com/@bewise9701/PyA07#main.py

from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        results = []
        job_list = soup.find_all("tr", class_="job")
        for item in job_list:
            job_tit = item.find("h2")
            job_title = job_tit.get_text(strip=True)


            job_com = item.find("h3")
            job_company = job_com.get_text(strip=True)

            job_tag = item.find("td", class_= "tags")
            tag = job_tag.get_text(strip=True)

            job_loca = item.find_all("div", class_="location")
            job_locations = []

            for location in job_loca:
                job_location = location.get_text(strip=True)
                job_locations.append(job_location)

            anchor = item.find('a')
            link = anchor['href']

            job_data = {
                'title': job_title,
                'link': f"https://remoteok.com/{link}",
                'tag': tag,
                'company': job_company,
                'location': job_locations
            }
            results.append(job_data)
        return results



    else:
        print("Can't get jobs.")

print(extract_jobs("react"))
