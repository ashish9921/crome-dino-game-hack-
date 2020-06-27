import pyautogui
from PIL import Image,ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def isColiddata(data):

   # for i in range(475,555):
     #   for j in range(210,290):

        #   if data[i,j]< 100:
           #     hit("down")  
           #     return True
                
    for i in range(465,555):
        for j in range(300,320):
            
            if data[i,j]<100:
                hit("up")
                return True
    return False         

    
if __name__=="__main__":
    time.sleep(3)
    hit("up")
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isColiddata(data)
            


       # for i in range(465,555):
          #  for j in range(298,320):
            #    data[i,j]=0


      #  for i in range(475,555):
       #     for j in range(210,290):
          #      data[i,j]=171        
      #  image.show()
      #  break
             