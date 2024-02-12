#   1:15 50

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty

#   1. can create a button that results in the label changing its text content 
class WidgetExample(GridLayout):
    count = 0
    my_text = StringProperty("0")
    
    def on_button_click(self):
        print("button clicked!")
        self.count += 1
        self.my_text = f"{self.count}"


class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.orientation ="lr-bt"

        for i in range(0,50):
            #if i == 5:
             #   b = Button(text="Hi",size_hint=(.2,.2))
              #  self.add_widget(b) 
               # continue
            #b = Button(text=str(i+1),size_hint=(.2,.2))
            b = Button(text=str(i+1),size_hint=(None,None), size = (dp(100),dp(100)))
            self.add_widget(b) 

#class GridLayourExample(GridLayout):
#    pass

class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        b1 = Button(text="Chubby")
        b2 = Button(text="Cheek")
        b3 = Button(text="Mai")
        
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """

class AnchorLayoutExample(AnchorLayout):
    pass

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()


"""
KV syntax

pos_hint: {"x":"y"}
    #   x takes in either:
           x, center_x, right 
           y, center_y, top
    sides of the button ( x = leftside, centerx = middle, right = rightside )
    #   y takes in either:
    percentage (0 - .9)
    #   size stays the same even when window size is changed

pos_size = x,y
    x takes width%?
    y takes height%
    if x/y takes in None, size wont change when window is being changed
    #   size changes proportional to window size

width: x
    returns width
height: y
    returns height

spacing: "x dp"
    creates some space between buttons

orientation: x or y
    takes in either vertical or horizontal

       

"""