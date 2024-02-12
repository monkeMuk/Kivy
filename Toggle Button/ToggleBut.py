#   2:20: 00
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line # for CanvasExample4
from kivy.graphics.context_instructions import Color #  for CanvasExample4
from kivy.graphics.vertex_instructions import Rectangle, Ellipse 
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.properties import StringProperty, BooleanProperty

class ToggleDisplay(GridLayout):

    count = 0
    count_enabled = BooleanProperty(False) 
    text = StringProperty("0")
    text_input_str = StringProperty("")
    #   slider_value_text = StringProperty("value")

    def button_press(self):
        if self.count_enabled == True:
            self.count += 1
            self.text = f"{self.count}"
        else:
            pass

    def toggle_button_on_state(self,widget):

        print("toggle state |   "+ widget.state)

        if widget.state == "down":
            #   ON
            widget.text = "ON"
            self.count_enabled = True
            
        else:
            #   OFF
            widget.text = "OFF"
            self.count_enabled = False
    
    def on_switch_active(self,widget):
        print(f"Switch: {widget.active}")
    
    def on_text_validate(self,widget):
        self.text_input_str = widget.text

    #def on_slider_value(self,widget):
        #print(f"Slider: {int(widget.value)}")
        #   self.slider_value_text = str(int(widget.value))
class TextText(GridLayout):
    text_input_str = StringProperty("")
    def on_text_validate(self,widget):
        self.text_input_str = widget.text

class BoxLayout(BoxLayout):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            Line(points = (0,0,300,500),width = 4)
            Color(1,1,0)
            Line(circle = (200,400,50),width = 4 )
            Color(0,1,1)
            Line(rectangle = (300,200,200,100),width = 4)
            self.rect = Rectangle(pos=(700,200),size=(200,100))
        
    def move_right(self):
        #print("mai")
        if self.rect.pos[0] + self.rect.size[0] < self.width:
            x,y = self.rect.pos
            x += dp(20)
            self.rect.pos = (x,y)
        else:
            pass
    
    def move_left(self):
        #print("mai")
        if self.rect.pos[0] > self.width-self.width:
            x,y = self.rect.pos
            x -= dp(20)
            self.rect.pos = (x,y)
        else:
            pass

class CanvasExample5(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.ball_size = dp(100)
        self.vx = dp(3)
        self.vy = dp(4  )

        with self.canvas:
            self.ball = Ellipse(pos =(self.center ),size=(self.ball_size, self.ball_size) )
        Clock.schedule_interval(self.update, 1/60)
        # counts every 1 second and does what def update does
        # refreshes at 1 time per second if it was (self.update, 1)
        # at 1/60 it does 

    def on_size(self,*args):
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)
        #   dont understand
    
    def update(self,dt):
        x,y = self.ball.pos

        x += self.vx
        y += self.vy 

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if x < 0:
            x = 0
            self.vx = -self.vx
            # need some workin
        if y < 0:
            y = 0 
            self.vy = -self.vy
            
        self.ball.pos = (x,y)

class CanvasExample6(Widget):
        pass
   
class Toggle(App):
    pass

Toggle().run() 