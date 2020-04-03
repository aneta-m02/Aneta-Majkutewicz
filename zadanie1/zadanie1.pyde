def draw():
    print(mouseX, mouseY, mousePressed)
    line(mouseX, mouseY, 100,100)
    if mousePressed:
        rect(mouseX, mouseY,100,100)
    else:
        rect(mouseX, mouseY, 50,50) # ten kwadrat jest przysłaniany po kliknięciu myszy więc nie ma sensu aby był rysowany w klatce gdzie następuje jej kliknięcie - optymalizacja poprzez mniej akcji dla programu, a ten sam efekt

# brakuje funkcji setup, użycia wbudowanych zmiennych height i width    
# 1,25 pkt
