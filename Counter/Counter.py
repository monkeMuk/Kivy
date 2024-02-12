from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class CounterTest(GridLayout):
    count = 0
    text = StringProperty("0")
    
    def button_press(self):
        print("button clicked!")
        self.count += 1
        self.text = f"{self.count}"
    

class Counter(App):
    pass

Counter().run()
