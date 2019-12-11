#def summa(a, b):
#    f=open("summa.txt", "w+")
#    try:
#        f.write(a + ";" + b)
##        f.close()
#        print("Salvestatud")
#    except:
#        print("Ebaõnnestus")
#    f.close()
#s=input("Sisestage summa: ")
#kp=input("Sisestage kuupäev: ")
#summa(s,kp)
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(Image.open('tsekk2.jpg'), lang="est"))