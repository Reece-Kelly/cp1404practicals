from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class MilesToKilometresApp(App):

    output_km = StringProperty

    def build(self):
        Window.size = (800, 500)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        print("calculate")
        miles = self.convert_string_to_float(text)
        self.update_label(miles)

    def handle_increment(self, text, change):
        print("increment")
        miles = self.convert_string_to_float(text) + change
        self.root.ids.input_number.text = str(miles)

    def update_label(self, miles):
        print("update label")
        kilometres = str(miles * 1.60934)
        self.root.ids.output_label.text = kilometres

    @staticmethod
    def convert_string_to_float(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometresApp().run()
