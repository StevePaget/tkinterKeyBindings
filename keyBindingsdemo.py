# Binding Keys demo


from tkinter import *
      
        


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.theCanvas = Canvas(self, width=650,height = 600, bg="#330000")
        self.theCanvas.grid(row=1, column=0, rowspan=6)
    
        self.bind("<Key>",self.keypressed)


    def keypressed(self,e):
        self.theCanvas.delete(ALL)
        self.theCanvas.create_text(300,300,text="Key " + repr(e.char) + " was pressed", fill="#FFFFFF")
        
        

if __name__ == "__main__":
    app = App()

