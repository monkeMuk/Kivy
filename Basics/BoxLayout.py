from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):
    def build(self):
        Layout = BoxLayout(
            orientation = "vertical",
            #   orientation = vertical/horizontal
            spacing = 10, 
            #   space between the buttons
            padding = [50,50]
            #   space between border and button
        )
        #   create buttons
        B2 = Button(text="B",size_hint = (.25,.25))
        B1 = Button(text="A",size_hint = (.25,.25))
        B3 = Button(text="C",size_hint = (.25,.25))

        
        #   display buttons
        Layout.add_widget(B1)
        Layout.add_widget(B2)
        Layout.add_widget(B3)


        return Layout



if __name__ == "__main__":
    BoxLayoutApp().run()
