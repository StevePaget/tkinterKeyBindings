# Binding Keys demo


from tkinter import *
      
        


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.theCanvas = Canvas(self, width=650,height = 600, bg="#330000")
        self.theCanvas.grid(row=1, column=0, rowspan=6)
    
        self.theCanvas.bind("<Key>",self.keypressed)


    def keypressed(self,e):
        print("!")
        print("Key ", repr(e.char), "was pressed")
        
        

if __name__ == "__main__":
    app = App()

