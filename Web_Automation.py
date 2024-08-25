from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# WebDriver'ı başlatın
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # ChromeDriver yolunu buraya yazın

# Web sayfasına gidin
driver.get('https://example.com/form')  # Web formunun URL'sini buraya yazın

# Form alanlarını bulun ve doldurun
name_field = driver.find_element(By.NAME, 'name')  # Alan adını 'name' ile değiştirin
email_field = driver.find_element(By.NAME, 'email')  # Alan adını 'email' ile değiştirin

name_field.send_keys('John Doe')
email_field.send_keys('john.doe@example.com')

# Formu gönderin
submit_button = driver.find_element(By.NAME, 'submit')  # Gönder butonunun alan adını 'submit' ile değiştirin
submit_button.click()

# Tarayıcıyı kapatın
driver.quit()
