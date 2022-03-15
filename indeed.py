import requests
from bs4 import BeautifulSoup


LIMIT = 50 
INDEED_URL=f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&start=0"



def get_last_page():
  result=requests.get(INDEED_URL)

  soup=BeautifulSoup(result.text,"html.parser")

  pagination=soup.find("div",{"class":"pagination"})

  links=pagination.find_all('a')
  pages=[]
  for link in links[:-1]:
    pages.append(int(link.string))

  max_page=pages[-1]
  return max_page

def get_jobs(last_page):
  jobs=[]
  for page in range(last_page):
    print(f"scraping page {page}")
    result=requests.get(f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25&start={page*10}")
    soup=BeautifulSoup(result.text,"html.parser")
    results=soup.find_all("a",{"class":"tapItem"})
    for result in results:
      job=extract_jobs(result)
      jobs.append(job)
  return jobs

def extract_jobs(html):
  title=html.find("h2",{"class":"jobTitle"}).find("span").string
  if title=="new":
    title=html.find("h2",{"class":"jobTitle"}).find_all("span")[1].string  
  company=html.find("div",{"class":"heading6 company_location tapItem-gutter companyInfo"}).find("span").string
  location=html.find("div",{"class":"companyLocation"}).string
  job_id=html["data-jk"]
  return {'title':title,'company':company,'location':location,'link':f"https://kr.indeed.com/채용보기?jk={job_id}"}

def scrape_jobs():
  last_page=get_last_page()

  jobs=get_jobs(last_page)

  return(jobs)