from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def scrape_indeed():
    job_results = []
    driver = None  # Initialize the driver variable
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('executable_path=C:\\Users\\inspired\\Desktop\Scraper\job_api')
        driver = webdriver.Chrome(options=chrome_options)
        
        driver.get('https://ng.indeed.com/jobs?q=customer+service&l=Nigeria&from=searchOnHP&vjk=0be98a4364a8bffc')
        
        # Use implicit wait to wait for elements to load
        driver.implicitly_wait(10)
        
        # Find the container holding job listings based on ID
        job_listings_container = driver.find_element(By.ID, '.jobsearch-Main')
        job_listings = job_listings_container.find_elements(By.CLASS_NAME, 'jobsearch-JapanPage')
        
       # Find job listings within the container
        for listing in job_listings:
            title_element = listing.find_element(By.CLASS_NAME, 'title')
            jcs_JobTitle = title_element.text
            
            company_element = listing.find_element(By.CLASS_NAME, 'company')
            companyInfo = company_element.text
            
            location_element = listing.find_element(By.CLASS_NAME, 'location')
            company_location = location_element.text
            
            job_results.append({'jcs_JobTitle': jcs_JobTitle, 'companyInfo': companyInfo, 'company_location': company_location})
        
        print("Scraping completed successfully")
        
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if driver is not None:
            driver.quit()
        
        return job_results

results = scrape_indeed()
for job in results:
    print(job)



 

