from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class ButtonAndEventslayout(GridLayout):
    text_input_str = StringProperty("")
    def submit_press(self):
        #   text_enabled = BooleanProperty(False)
        #   if text_enabled == False:
        pass

    def on_text_validate(self,widget):
        self.text_input_str = widget.text

    #def build(self):
     
     #   layout = GridLayout(

      #  orientation = "lr-tb",
       #     cols = 2,
        #    rows = 3
         #   )

        #label_1 = Label(text="First Name")
        #question_1 = TextInput(multiline = False)
        #label_2 = Label(text="Last Name")
        #question_2 = TextInput(multiline = False)
        #label_3 = Label(text="Email")
        #question_3 = TextInput(multiline = False)
        
        #button1 = Button(text="Submit",font_size = 50,pos=(.5,1))
       
         
        #layout.add_widget(label_1)
        #layout.add_widget(question_1)
        #layout.add_widget(label_2)
        #layout.add_widget(question_2)
        #layout.add_widget(label_3)
        #layout.add_widget(question_3)
        #layout.add_widget(button1)

        

        #return layout
    

class ButtonAndEventsApp(App):
    pass

if __name__=="__main__":
    ButtonAndEventsApp().run()