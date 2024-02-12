from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class BoxLayoutApp(App):
    def build(self):
        Layout = GridLayout(
            cols = 2,
            rows = 2,
            orientation = "lr-tb",
            #   orientation = left/right - top/bottom
            spacing = 10,
            padding = 20
            
           
        )
        #   create buttons
        A = Button(text="A")
        B = Button(text="B")
        C = Button(text="C")
        D = Button(text="D")

        
        #   display buttons
        Layout.add_widget(A)
        Layout.add_widget(B)
        Layout.add_widget(C)
        Layout.add_widget(D)


        return Layout



if __name__ == "__main__":
    BoxLayoutApp().run()
