def setup():
    size(500, 500)
    frameRate(50)
    global slownik_kolorow
    slownik_kolorow = {"niebieski":(3, 169, 252, 100), "różowy":(252, 3, 198, 100), "żółty":(252, 248, 3,100)}
    global lista_kolorow
    lista_kolorow = []
    for klucz, wartosc in slownik_kolorow.items(): 
        lista_kolorow.append(wartosc) 
    global iteracja_programu
    iteracja_programu = 430

def draw():          
    stroke(252, 3, 198, 100)                
    stroke(*slownik_kolorow["niebieski"])
    point(width/100,height/100)           
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    global iteracja_programu
    iteracja_programu -=1
    rect(iteracja_programu, iteracja_programu, 70,70)
    rect(0, iteracja_programu, 70,70)
    if mousePressed:
        exit()
