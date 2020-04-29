def setup():
    size(400, 400)
    textSize(40)
    global slownik_kolorow
    slownik_kolorow = {"niebieski":(43, 181, 255), "fioletowy":(163, 43, 250), "żółty":(243, 250, 40)}
def draw():
    clear()
    text("A", width/2-65, height-194)
    print(hex(get(mouseX, mouseY)))
    text("M", width/2+20, height-242)
    print(hex(get(mouseX, mouseY)))               
    global slownik_kolorow
    fill(*slownik_kolorow["niebieski"])           
    if mousePressed:   # miało być na najechanie, nie kliknięcie      
       global slownik_kolorow
       fill(*slownik_kolorow["fioletowy"])        
    if keyPressed: # powinno być doprecyzowane na jakie klawisze
       global slownik_kolorow               
       fill(*slownik_kolorow["żółty"])       
    s = createShape() 
    s.beginShape()
    s.fill(255, 0, 0) 
    s.vertex(1, height/5*5)
    s.vertex(width/1, height/5*5)
    s.vertex(width/40, height/3*5+10)
    s.vertex(width-40, height/5)
    s.endShape(CLOSE) 
    shape( s, 140, 50, width/2-80,height/2)
    # ładna kompozycja
    
#0,75p
