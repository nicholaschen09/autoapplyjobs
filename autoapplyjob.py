from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Setup the Safari driver
driver = webdriver.Safari()

# Function to login to LinkedIn (or another job board)
def login_to_linkedin(email, password):
    driver.get("https://www.linkedin.com/login")
    sleep(2)
    email_input = driver.find_element("id", "username")
    email_input.send_keys(email)
    password_input = driver.find_element("id", "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    sleep(3)

# Function to apply to jobs
def apply_to_job(job_title): 
    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={job_title.replace(' ', '%20')}")
    sleep(2)

    # Example loop through job postings (simplified)
    jobs = driver.find_elements("css selector", ".job-card-container")
    for job in jobs:
        try:
            job.click()
            sleep(2)
            apply_button = driver.find_element("css selector", ".jobs-apply-button")
            apply_button.click()
            sleep(2)

            # Fill out application forms if needed
            # submit_button = driver.find_element("css selector", "button[aria-label='Submit application']")
            # submit_button.click()
            sleep(2)
        except Exception as e:
            print(f"Error applying to job: {e}")

# Run the functions
login_to_linkedin("email", "password") //change these based on whatever your info is
apply_to_job("Software Developer") //change these based on whatever you need
driver.quit()
