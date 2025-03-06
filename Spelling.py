import keyboard
import pyautogui
import cv2
import pytesseract

def on_ctrl_press(event):
    #Screenshot the Text
    go = pyautogui.screenshot(region=(500,10,800,80))
    image_path = r"C:\Users\Miguel Estrada\Videos\MigZCode\Scripts\SpellingBee.png"
    go.save(image_path)
    
    #Extract the Text from the image
    img = cv2.imread(image_path)
    pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Miguel Estrada\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
    word = pytesseract.image_to_string(img)
    word = word.replace('.','')
    last_word = word.split()[-1]
    
    print(last_word)
    
    #Typing
    pyautogui.write(str(last_word), interval=0.06)

def on_esc_press(event):
    print("Exiting")
    exit(0)
    
keyboard.on_press_key('ctrl', on_ctrl_press)
keyboard.on_press_key('esc', on_esc_press)

print("Press 'ctrl' to run and press 'esc' to exit")
keyboard.wait('/')