def draw():
    print(mouseX, mouseY, mousePressed)
    line(mouseX, mouseY, 100,100)
    rect(mouseX, mouseY, 50,50)
    if mousePressed:
        rect(mouseX, mouseY,100,100)
