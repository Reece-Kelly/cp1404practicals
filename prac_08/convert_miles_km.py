from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KILOMETRES_FACTOR = 1.60934


class MilesToKilometresApp(App):
    output_km = StringProperty

    def build(self):
        """Build the Kivy app from a kv file."""
        Window.size = (800, 500)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation miles to kilometres."""
        print("calculate")
        miles = self.convert_string_to_float(text)
        self.update_label(miles)

    def handle_increment(self, text, change):
        """Handle up and down button press and update text input."""
        print("increment")
        miles = self.convert_string_to_float(text) + change
        self.root.ids.input_number.text = str(miles)

    def update_label(self, miles):
        print("update label")
        kilometres = str(miles * MILES_TO_KILOMETRES_FACTOR)
        self.root.ids.output_label.text = kilometres

    @staticmethod
    def convert_string_to_float(text):
        """Convert string to a float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesToKilometresApp().run()
