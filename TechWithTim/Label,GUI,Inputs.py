
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LabelGuiInputsApp(App):
    def build(self):

        layout = GridLayout(
            orientation = "lr-tb",
            cols = 2,
            rows = 3

        )

        label_1 = Label(text="First Name")
        question_1 = TextInput(multiline = False)
        label_2 = Label(text="Last Name")
        question_2 = TextInput(multiline = False)
        label_3 = Label(text="Email")
        question_3 = TextInput(multiline = False)
       
         
        layout.add_widget(label_1)
        layout.add_widget(question_1)
        layout.add_widget(label_2)
        layout.add_widget(question_2)
        layout.add_widget(label_3)
        layout.add_widget(question_3)
        

        return layout


if __name__=="__main__":
    LabelGuiInputsApp().run()