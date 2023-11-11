from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Reece", "Sean", "Jillian", "Jace"]

    def build(self):
        """Build the Kivy app from a kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Labels from a list and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
