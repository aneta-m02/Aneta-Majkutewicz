class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): 
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space

# brak dodatkowej klasy, a to ją bym oceniała
            
def setup():
    size(500, 500)
    global slownik_kolorow
    slownik_kolorow = {"niebieski":(43, 181, 255), "fioletowy":(163, 43, 250), "żółty":(243, 250, 40), "różowy":(252, 3, 198, 100), "zielony":(63, 255, 46)}
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300) 
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyKwadrat.sketch(123, 153) 
    malyPasiastyKwadrat = PasiastyKwadrat(50.0)
    malyPasiastyKwadrat.sketchPasiasty(400, 300, 5)
    malyPasiastyKwadrat.sketchPasiasty(50,300, 8) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(350, 100, 12)
    duzyPasiastyKwadrat.sketch(200, 370)

def draw():
    malyKwadrat = Kwadrat(50.0) 
    malyKwadrat.sketch(200, 300)
    fill(*slownik_kolorow["fioletowy"])     
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    fill(*slownik_kolorow["żółty"])
    malyKwadrat.sketch(123, 153)  
    malyPasiastyKwadrat = PasiastyKwadrat(50.0)
    fill(*slownik_kolorow["różowy"]) 
    malyPasiastyKwadrat.sketchPasiasty(400, 300, 5)
    fill(*slownik_kolorow["niebieski"]) 
    malyPasiastyKwadrat.sketchPasiasty(50,300, 8) 
    fill(*slownik_kolorow["zielony"]) 
    duzyPasiastyKwadrat  = PasiastyKwadrat(120.0)
    duzyPasiastyKwadrat.sketchPasiasty(350, 100, 12)
    fill(*slownik_kolorow["żółty"])
    duzyPasiastyKwadrat.sketch(200, 370)
    fill(*slownik_kolorow["niebieski"])
    
#brak zrozumienia polecenia jest tu gorszym przewinieniem... 0pkt
