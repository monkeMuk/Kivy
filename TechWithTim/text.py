from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class testy2(GridLayout):
    pass
    text_input_str = StringProperty("")
    def on_text_validate(self,widget):
        self.text_input_str = widget.text
    

class testApp(App):
    pass

testApp().run()