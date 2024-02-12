
#   NEEDS FURTHER CHECKING
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class AnchorLayoutApp(App):
    def build(self):
        #   create Layout
        #   it "sticks it  to a desired corner"
        Layout = AnchorLayout(
            anchor_x = "left",
            anchor_y = "bottom"
            )
        Layout2 = AnchorLayout(
            anchor_x = "right",
            anchor_y = "bottom"
            )
        #   create button
        B1 = Button(text="Hi",size_hint=(.25,.25))
        B2 = Button(text="mAI",size_hint=(.25,.25))

        #   add button to layout
        Layout.add_widget(B1)
        Layout2.add_widget(B2)

        return Layout#,Layout2


    

        
if __name__ =="__main__":
    AnchorLayoutApp().run()