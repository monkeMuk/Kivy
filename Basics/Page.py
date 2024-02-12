from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class PageLayoutApp(App):
    def build(self):
        layout = PageLayout()

        layout.add_widget(Button(text="Main"))
        layout.add_widget(Button(text="Page_1"))
        layout.add_widget(Button(text="Page_2"))

        return layout

if __name__ == "__main__":
    PageLayoutApp().run()
