import os
import shutil
import time
from pathlib import Path
from io import BytesIO
from PIL import Image
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RobotCustomizer:
    def __init__(self):
        self.output_dir = Path(__file__).resolve().parent / "images"
        self.current_image = None
        self.browser = webdriver.Chrome()
        self.browser.get("https://robotsparebinindustries.com/")
        self.clean_output()
        self.setup_output()

    def clean_output(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def setup_output(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def order(self):
        nav_links = self.browser.find_elements(By.CLASS_NAME, "nav-link")
        nav_links[-1].click()

    def wait_for(self, xpath):
        return EC.visibility_of_element_located((By.XPATH, xpath))(self.browser)

    def close_modal(self):
        self.wait_for("//button[text()='OK']").click()

    def customize(self, data):
        head, body, legs, address = data
        self.browser.find_element(By.XPATH, f"//option[@value='{head}']").click()
        self.browser.find_element(
            By.XPATH, f"//input[@value='{body}']/ancestor::label"
        ).click()
        self.browser.find_elements(By.CLASS_NAME, "form-control")[0].send_keys(legs)
        self.browser.find_elements(By.CLASS_NAME, "form-control")[1].send_keys(address)
        time.sleep(1)

    def preview(self):
        while True:
            try:
                self.browser.find_element(By.ID, "preview").click()
                self.wait_for("//div[@id='robot-preview-image']")
                break
            except:
                pass

    def place_order(self):

        error_msg = (By.CSS_SELECTOR, ".alert.alert-danger")

        while True:
            try:
                self.browser.find_element(By.ID, "order").click()
            except:
                pass

            try:
                WebDriverWait(self.browser, 1).until(
                    EC.invisibility_of_element(error_msg)
                )
                break
            except:
                pass

    def wait_for(self, xpath):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def get_status(self):
        xpath = "//p[@class='badge badge-success']"

        element = self.wait_for_element(xpath)
        if element:
            return element.text
        else:
            return ""

    def wait_for_element(self, xpath):
        wait = WebDriverWait(self.browser, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element

    def generate_image(self, data):
        urls = [
            f"https://robotsparebinindustries.com/{part}/{data[i]}.png"
            for i, part in enumerate(["heads", "bodies", "legs"])
        ]

        images = []
        for url in urls:
            img = Image.open(BytesIO(requests.get(url).content))
            img = img.resize((354, 200))
            images.append(img)

        combined = Image.new(
            "RGB", (max(img.width for img in images), sum(img.height for img in images))
        )

        y = 0
        for img in images:
            combined.paste(img, (0, y))
            y += img.height

        self.current_image = combined

    def save_image(self):
        status = self.get_status()
        new_filename = f"_{status}_robot.jpg"
        new_filename = new_filename.replace("_RSB-ROBO-ORDER-", "")
        self.current_image.save(self.output_dir / new_filename)

    def process(self):
        data = self.get_data("https://robotsparebinindustries.com/")
        for item in data:
            self.close_modal()
            self.customize(item)
            self.preview()
            self.generate_image(item)
            self.place_order()
            self.save_image()
            self.next()

    def click_make_order(self):
        try:
            while True:
                order_button = self.driver.find_element(
                    By.XPATH, '//button[@id="order"]'
                )
                self.driver.execute_script("arguments[0].click();", order_button)
        except Exception:
            pass

    def get_data(self, url):
        response = requests.get(url + "orders.csv")
        data = response.text.split("\n")[1:]
        return [d.split(",")[1:] for d in data]

    def next(self):
        self.browser.find_element(By.ID, "order-another").click()

    def start(self):
        self.order()
        self.process()


bot = RobotCustomizer()
bot.start()
bot.browser.quit()