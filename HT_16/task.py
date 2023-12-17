import os
import shutil
import time as t
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pathlib import Path
from io import BytesIO as B
from PIL import Image
import requests as r
from selenium import webdriver as w
from selenium.webdriver.common.by import By as Byy
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.wait import WebDriverWait as W


class CustomRobot:
    def __init__(self):
        self.output_directory = Path(__file__).resolve().parent / "images"
        self.current_image = None
        self.browser = w.Chrome()
        self.browser.get("https://robotsparebinindustries.com/")
        self.clean_output()
        self.prepare_output()

    def clean_output(self):
        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)

    def prepare_output(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def make_order(self):
        nav_links = self.browser.find_elements(Byy.CLASS_NAME, "nav-link")
        nav_links[-1].click()

    def wait_for_element(self, xpath):
        return E.visibility_of_element_located((Byy.XPATH, xpath))(self.browser)

    def close_popup(self):
        self.wait_for_element("//button[text()='OK']").click()

    def customize_robot(self, data):
        head, body, legs, address = data
        self.browser.find_element(Byy.XPATH, f"//option[@value='{head}']").click()
        self.browser.find_element(
            Byy.XPATH, f"//input[@value='{body}']/ancestor::label"
        ).click()
        self.browser.find_elements(Byy.CLASS_NAME, "form-control")[0].send_keys(legs)
        self.browser.find_elements(Byy.CLASS_NAME, "form-control")[1].send_keys(address)
        t.sleep(1)

    def preview_robot(self):
        while True:
            try:
                self.browser.find_element(Byy.ID, "preview").click()
                self.wait_for_element("//div[@id='robot-preview-image']")
                break
            except Exception:
                pass

    def place_order(self):
        error_msg = (Byy.CSS_SELECTOR, ".alert.alert-danger")

        while True:
            try:
                self.browser.find_element(Byy.ID, "order").click()
            except Exception:
                pass

            try:
                W(self.browser, 1).until(E.invisibility_of_element(error_msg))
                break
            except Exception:
                pass

    def check_status(self):
        xpath = "//p[@class='badge badge-success']"

        element = self.wait_for_element(xpath)
        if element:
            return element.text
        else:
            return ""

    def get_element(self, xpath):
        wait = W(self.browser, 20)
        element = wait.until(E.visibility_of_element_located((Byy.XPATH, xpath)))
        return element

    def create_robot_image(self, data):
        urls = [
            f"https://robotsparebinindustries.com/{part}/{data[i]}.png"
            for i, part in enumerate(["heads", "bodies", "legs"])
        ]

        images = []
        for url in urls:
            img = Image.open(B(r.get(url).content))
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

    def save_robot_image(self):
        status = self.check_status()
        # new_filename = f"_{status}_robot.jpg"
        # new_filename = new_filename.replace("_RSB-ROBO-ORDER-", "")
        # self.current_image.save(self.output_directory / new_filename)
        self.current_image.save(self.output_directory / f"_{status}_robot.jpg")

    def save_to_pdf(self, html_code):
        status = self.check_status()
        filename = f"{status}_robot.pdf"
        pdf_path = self.output_directory / filename

        c = canvas.Canvas(str(pdf_path), pagesize=letter)
        c.drawString(100, 750, "HTML Code:")
        c.drawString(100, 730, html_code)
        c.drawString(100, 700, "Robot Image:")

        if self.current_image:
            image_path = self.output_directory / f"_{status}_robot.jpg"
            c.drawImage(str(image_path), 100, 500, width=200, height=200)

        c.save()

    def process_order(self):
        data = self.order_data("https://robotsparebinindustries.com/")
        for item in data:
            self.close_popup()
            self.customize_robot(item)
            self.preview_robot()
            self.create_robot_image(item)
            self.place_order()
            self.save_robot_image()
            html_code = self.browser.page_source
            self.save_to_pdf(html_code)
            self.proceed()

    def initiate_order(self):
        try:
            while True:
                order_button = self.browser.find_element(Byy.XPATH, '//button[@id="order"]')
                self.browser.execute_script("arguments[0].click();", order_button)
        except Exception:
            pass

    def order_data(self, url):
        response = r.get(url + "orders.csv")
        data = response.text.split("\n")[1:]
        return [d.split(",")[1:] for d in data]

    def proceed(self):
        self.browser.find_element(Byy.ID, "order-another").click()

    def start(self):
        self.make_order()
        self.process_order()


robot = CustomRobot()
robot.start()
robot.browser.quit()

