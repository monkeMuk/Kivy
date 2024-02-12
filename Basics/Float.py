from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class FloatLayoutApp(App):
    def build(self):
        Layout = FloatLayout()
        #   float allows pos_hint
        # pos_hint requires dict// pos_hint={center_x:x,center_y:y}
        #   create buttons
        
        B1 = Button(text="A",size_hint = (.25,.25),pos_hint={"center_x":.75,"center_y":.25})
        B2 = Button(text="B",size_hint = (.25,.25),pos_hint={"center_x":.25,"center_y":.5})

        
        #   display buttons
        Layout.add_widget(B1)
        Layout.add_widget(B2)


        return Layout



if __name__ == "__main__":
    FloatLayoutApp().run()
