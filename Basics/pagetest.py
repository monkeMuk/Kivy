from typing import Sized
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty 
from kivy.uix.popup import Popup 


class MyImage(Image):
     
    planeimg = ObjectProperty(None)
    planeimg2 = ObjectProperty(None)
    planeimg3 = ObjectProperty(None)
    planeimg4 = ObjectProperty(None )

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            
            if self.source == "plane.png":
                touch.grab(self)
                pop = Popup(
                    title= "Plane",
                    content=Image(source="plane.png"),
                    size_hint=(.5,.5),)
                pop.open()
                return True

            if self.source == "plane2.png":
                touch.grab(self)
                pop = Popup(
                    title= "Plane2",
                    content=Image(source="plane2.png"),
                    size_hint=(.5,.5),)
                pop.open()
                return True

            if self.source == "plane3.jpeg":
                touch.grab(self)
                pop = Popup(
                    title= "Plane3",
                    content=Image(source="plane3.jpeg"),
                    size_hint=(.5,.5),)
                pop.open()
                return True

            if self.source == "plane4.jpeg":
                touch.grab(self)
                pop = Popup(
                    title= "Plane4",
                    content=Image(source="plane4.jpeg"),
                    size_hint=(.5,.5),)
                pop.open()
                return True

        return super(MyImage,self).on_touch_down(touch)
        
    def on_touch_up(self, touch):
        pass

class PageLayoutTest(PageLayout):
    pass

class PageApp(App):
    def build(self):
        return PageLayoutTest()

if __name__ == "__main__":
    PageApp().run()
