import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DragDrop:
    def __init__(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()
        # Open the jQuery UI droppable demo page
        self.driver.get("https://jqueryui.com/droppable/")
        # Maximize the browser window
        self.driver.maximize_window()

    def switch_to_iframe(self):
        # Wait for the iframe to be present and switch to it
        iframe_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@class='demo-frame']"))
        )
        self.driver.switch_to.frame(iframe_element)

    def drag_and_drop(self):
        # Wait for the draggable element to be present
        draggable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "draggable"))
        )
        # Wait for the droppable element to be present
        destination = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "droppable"))
        )
        # Adding a sleep to observe the action (not recommended for actual test scripts)
        time.sleep(10)
        # Perform drag and drop action
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, destination).perform()
        # Adding a sleep to observe the result (not recommended for actual test scripts)
        time.sleep(10)
        print("Drag and drop functionality working successfully!!")

    def quit_driver(self):
        # Close the browser and quit the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    # Create an instance of the DragDrop class
    drag_drop_instance = DragDrop()
    # Switch to the iframe containing the draggable and droppable elements
    drag_drop_instance.switch_to_iframe()
    # Perform the drag and drop action
    drag_drop_instance.drag_and_drop()
    # Wait to see the result before closing the browser
    time.sleep(5)
    # Quit the WebDriver
    drag_drop_instance.quit_driver()
