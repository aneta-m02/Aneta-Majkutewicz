import random
add_library('pdf')

def setup():
    global img
    size(400,400) #brak proporcji zdjęcia dokumentowego
    img= loadImage("dowod.jpg")
    beginRecord(PDF, "photo.pdf")
    image(img, 0,0, height, width)
    print(random.random())
    print(type(img))

          
def draw():
    global img
    if mousePressed:
       img= loadImage("07.png")
       #beginRecord(PDF, "motyl1.pdf")
       image(img, 300,100, height-300, width-300)
       endRecord()
    if keyPressed:
       img= loadImage("08.png")
       #beginRecord(PDF, "motyl2.pdf")
       image(img, 0,287, height-300, width-300)
       endRecord()
# zaczynasz nagrywać zawartość pdf'a w trzech miejscach a kończysz w dwóch?
# 1,5p
