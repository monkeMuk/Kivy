#3: 00: 57
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.app import App


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    #   variable that can also be changed in .kv file 

    V_NB_LINES = 7
    V_LINES_SPACING = .1 #   space between the lines/ percentage in screen width
    vertical_lines = []    #   ?

    def __init__(self,**kwargs):
        super(MainWidget,self).__init__(**kwargs)   # don get it?
        #print(f"INIT w: {self.width} INIT h: {self.height}")
        self.init_vertical_lines()
    
    def on_parent(self,widget,parent):
        #print(f"INIT w: {self.width} INIT h: {self.height}")
        pass
    def on_size(self, *args):
        #print(f"ON SIZE w: {self.width} ON SIZE h: {self.height}")
        #self.perspective_point_x = self.width/2
        #self.perspective_point_y = self.height*3/4
        self.update_vertical_lines()

    def on_perspective_point_x(self,widget,value):
        #print(f"PX: {self.perspective_point_x}")
        pass
    def on_perspective_point_y(self,widget,value):
        #print(f"PY: {self.perspective_point_y}")
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            #self.line = Line(points = [100,0,100,100] ) #   to use later to draw the line at the middle
            for i in range(0,self.V_NB_LINES): #    create new lines from V_NB_LINES
                self.vertical_lines.append(Line())      #   adds the new line into vertical_line

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING * self.width   
        offset = -int(self.V_NB_LINES/2)
        

        for i in range(0,self.V_NB_LINES): #    create new lines from V_NB_LINES
            line_x = int(central_line_x + offset*spacing)
            self.vertical_lines[i].points =  [line_x,0,line_x,self.height]
            offset += 1 
            #   This creates 7 horizontal lines pointing above
      
class GalaxyApp(App):
    pass

GalaxyApp().run()