import os
import random
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from PIL import Image
import pytesseract
from io import BytesIO

# Calea către executabil
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Calea exactă către folderul unde se află eng.traineddata
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'emulator-5554'
options.app_package = 'com.tpcstld.twozerogame'
options.app_activity = 'com.tpcstld.twozerogame.MainActivity'
options.no_reset = True

driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
time.sleep(2)

driver.execute_script('mobile: clickGesture', {
    'x': 995,
    'y': 750
})
time.sleep(1)

driver.execute_script('mobile: clickGesture', {
    'x': 909,
    'y': 1353
})
time.sleep(1)

directii = ['up', 'down', 'left', 'right']

for i in range(10):
    directie = random.choice(directii)
    print(f"Swipe {i+1}: {directie}")
    
    driver.execute_script('mobile: swipeGesture', {
        'left': 100,
        'top': 300,
        'width': 500,
        'height': 500,
        'direction': directie,
        'percent': 0.75
    })
    time.sleep(0.5)

print("Aștept 5 secunde...")
time.sleep(5)

driver.execute_script('mobile: clickGesture', {
    'x': 995,
    'y': 750
})
time.sleep(1)

driver.execute_script('mobile: clickGesture', {
    'x': 909,
    'y': 1353
})
time.sleep(2) 

screenshot = driver.get_screenshot_as_png()
imagine = Image.open(BytesIO(screenshot))
zona_scor = imagine.crop((677, 583, 770, 642))

config_tesseract = r'--psm 6 -c tessedit_char_whitelist=0123456789'
scor_text = pytesseract.image_to_string(zona_scor, config=config_tesseract).strip()

print(f"Scorul citit este: '{scor_text}'")
assert scor_text == '0', f"Eroare: Scorul e {scor_text}, nu 0!"
print("Test trecut: Scorul s-a resetat la 0.")

driver.quit()