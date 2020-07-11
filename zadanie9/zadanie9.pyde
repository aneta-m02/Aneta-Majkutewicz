def setup():
    size(600,600)
    global img
    img = loadImage("Piesek1.jpg")
    background(250, 211, 55)
    strokeWeight(7)
    
def draw():
    global img
    try:
        image(img, 130, 130, 340, 340)
    except:
        fill(181, 36, 36)
        text("Nie mozna wczytac obrazu", width/2-73, height/2)
        stroke(232, 39, 62)
    else:
        stroke(59, 209, 255)
    finally:
        noFill()
        square(130, 130, 340)
