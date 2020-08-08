import cv2
import pytesseract
import os
import sys


#Load Images
for files in os.listdir():
    print(files)                
    
IMAGE = input("Select image: ")


#Check for .txt file and print and search contents if it exists
IMAGETXT = f'{IMAGE}.txt'
for files in os.listdir():
    if files == IMAGETXT:
        f = open(f'{IMAGETXT}', 'r')     
        file_contents = f.read()
        print(file_contents)
        keyword1 = input("Keyword: ")
        search = file_contents.find(keyword1)
        print(file_contents[search-100:500])
        sys.exit()       

#Image to text
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread(IMAGE)
text = pytesseract.image_to_string(img)

#Saving the text for later use | **Do this later**
data_file = open(f'{IMAGE}.txt', 'w')
data_file.write(text)


#Finding stuff in texts
print(text)
keyword2 = input("Keyword: ")
search = text.find(keyword2)
print(text[search-100:500])

