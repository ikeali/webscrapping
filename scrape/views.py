# from django.shortcuts import render
# import requests
# # from bs4 import BeautifulSoup
# from django.conf import settings  # Import settings from django.conf
# from django.http import JsonResponse
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


from django.http import JsonResponse
from .scraping_utils import scrape_indeed



def get_jobs(request):
    scraped_jobs = scrape_indeed()
    return JsonResponse(scraped_jobs, safe=False)







# def scrape_indeed(request):
#     # url = "https://ng.indeed.com/?hl=en&co=ng&countrySelector=1&_ga=2.174503588.767820975.1691882065-1988928636.1690286163"
#     url = "https://www.indeed.com/jobs?q=receptionist&l=sandia+park%2C+nm&from=searchOnHP&vjk=73b99d1fd0260bcc"
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url,headers=headers)


#     if response.status_code == 200:
#         html = response.content
#     else:
#         return JsonResponse({'error': f'Failed to retrieve data from Indeed ,{response.status_code}{response.content}'})

#     soup = BeautifulSoup(html, 'html.parser')
#     job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
#     jobs = []
#     for job in job_listings:
#         title = job.find('h2', class_='title').text.strip()
#         company = job.find('span', class_='company').text.strip()
#         location = job.find('span', class_='location').text.strip()

#         jobs.append({
#             'title': title,
#             'company': company,
#             'location': location,
#         })

#     return JsonResponse({'jobs': jobs})



# def scrape_glassdoor(request):
#     # url = "https://ng.indeed.com/?hl=en&co=ng&countrySelector=1&_ga=2.174503588.767820975.1691882065-1988928636.1690286163"
#     url = "https://www.glassdoor.com/Job/index.htm"
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     response = requests.get(url,headers=headers)


#     if response.status_code == 200:
#         html = response.text
#     else:
#         return JsonResponse({'error': 'Failed to retrieve data from Glassdoor'})

#     soup = BeautifulSoup(html, 'html.parser')
#     job_listings = soup.find_all('div', class_='jobsearch-SerpJobCard')
#     jobs = []
#     for job in job_listings:
#         title = job.find('h2', class_='title').text.strip()
#         company = job.find('span', class_='company').text.strip()
#         location = job.find('span', class_='location').text.strip()

#         jobs.append({
#             'title': title,
#             'company': company,
#             'location': location,
#         })

#     return JsonResponse({'jobs': jobs})



    
