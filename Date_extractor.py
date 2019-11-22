from PIL import Image
import pytesseract
import cv2
import re
import datefinder
from dateparser.search import search_dates


        
def date_find(path =0, url = 0):
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\MEGAMODZ\AppData\Local\Tesseract-OCR\tesseract.exe'
    text0 = pytesseract.image_to_string(path, config = '--psm 11 --oem 3')
    text1 = pytesseract.image_to_string(path)
    text_extract1 =" ".join(text0.splitlines())
    text_extract2 =" ".join(text1.splitlines())
    text123 = text_extract1.split(' ')
    text234 = text_extract2.split(' ')
    x,y = sep(text123),sep(text234)
    #print(x,y)
    if x != y:
        if x != None:
            return x
        else:
            return y
    elif x and y == None:
        return "None"
    else:
        return x
        
    
    
def sep(text):
    k = []
    for i in text:
        if i.count('/') in range(2,4):
            k.append(i)
        elif i.count('-') in range(2,4): 
            k.append(i)
        elif "'" in i:
            k.append(i)
        elif "’" in i:
            k.append(i)
        else:
            continue   
    l = ' '.join(k)
    l = search_dates(l)
    if l != None:
        for j in l[0]:
            H = search_dates(j)
            if H == None:
                return None
            else:
                for i in H:
                    j = i[1].date()
                    j = i[1].strftime('%Y/%m/%d')
                    return j
    else :
        return None

            

        

