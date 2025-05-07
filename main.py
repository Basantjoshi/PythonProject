from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("calculator.kv")

class LandConverter(BoxLayout):
    def clear_result(self, label_id):
        # Clear the text of the specified result label
        if label_id in self.ids:
            self.ids[label_id].text = ""

    def show_result(self, label_id, result_text):
        # Show the result by setting the text of the specified label
        if label_id in self.ids:
            self.ids[label_id].text = result_text

    def rapd_to_sqft(self, r, a, p, d):
        return (r * 5476) + (a * 342.25) + (p * 85.56) + (d * 21.39)

    def sqft_to_rapd(self, sqft):
        r = int(sqft // 5476)
        sqft %= 5476
        a = int(sqft // 342.25)
        sqft %= 342.25
        p = int(sqft // 85.56)
        sqft %= 85.56
        d = round(sqft / 21.39)
        return r, a, p, d

    def bkd_to_sqft(self, b, k, d):
        return (b * 72900) + (k * 3645) + (d * 182.25)

    def sqft_to_bkd(self, sqft):
        b = int(sqft // 72900)
        sqft %= 72900
        k = int(sqft // 3645)
        sqft %= 3645
        d = round(sqft / 182.25)
        return b, k, d

    def rapd_to_sqm(self, r, a, p, d):
        sqft = self.rapd_to_sqft(r, a, p, d)
        return sqft * 0.092903

    def sqm_to_rapd(self, sqm):
        sqft = sqm * 10.7639
        return self.sqft_to_rapd(sqft)

    def bkd_to_sqm(self, b, k, d):
        sqft = self.bkd_to_sqft(b, k, d)
        return sqft * 0.092903

    def sqm_to_bkd(self, sqm):
        sqft = sqm * 10.7639
        return self.sqft_to_bkd(sqft)

    def convert_rapd_to_sqft(self):
        try:
            r = int(self.ids.ropani.text or 0)
            a = int(self.ids.aana.text or 0)
            p = int(self.ids.paisa.text or 0)
            d = int(self.ids.daam.text or 0)
            sqft = self.rapd_to_sqft(r, a, p, d)
            self.clear_result('result_rapd_to_sqft')
            self.show_result('result_rapd_to_sqft', f"Result: {sqft:.2f} sq.ft")
        except ValueError:
            self.clear_result('result_rapd_to_sqft')
            self.show_result('result_rapd_to_sqft', "Result: Invalid input")

    def convert_sqft_to_rapd(self):
        try:
            sqft = float(self.ids.sqft_rapd.text or 0)
            r, a, p, d = self.sqft_to_rapd(sqft)
            self.clear_result('result_sqft_to_rapd')
            self.show_result('result_sqft_to_rapd', f"Result: {r} Ropani {a} Aana {p} Paisa {d} Daam")
        except ValueError:
            self.clear_result('result_sqft_to_rapd')
            self.show_result('result_sqft_to_rapd', "Result: Invalid input")

    def convert_rapd_to_sqm(self):
        try:
            r = int(self.ids.ropani.text or 0)
            a = int(self.ids.aana.text or 0)
            p = int(self.ids.paisa.text or 0)
            d = int(self.ids.daam.text or 0)
            sqm = self.rapd_to_sqm(r, a, p, d)
            self.clear_result('result_rapd_to_sqm')
            self.show_result('result_rapd_to_sqm', f"Result: {sqm:.2f} sq.m")
        except ValueError:
            self.clear_result('result_rapd_to_sqm')
            self.show_result('result_rapd_to_sqm', "Result: Invalid input")

    def convert_sqm_to_rapd(self):
        try:
            sqm = float(self.ids.sqm_rapd.text or 0)
            r, a, p, d = self.sqm_to_rapd(sqm)
            self.clear_result('result_sqm_to_rapd')
            self.show_result('result_sqm_to_rapd', f"Result: {r} Ropani {a} Aana {p} Paisa {d} Daam")
        except ValueError:
            self.clear_result('result_sqm_to_rapd')
            self.show_result('result_sqm_to_rapd', "Result: Invalid input")

    def convert_bkd_to_sqft(self):
        try:
            b = int(self.ids.bigha.text or 0)
            k = int(self.ids.kattha.text or 0)
            d = int(self.ids.dhur.text or 0)
            sqft = self.bkd_to_sqft(b, k, d)
            self.clear_result('result_bkd_to_sqft')
            self.show_result('result_bkd_to_sqft', f"Result: {sqft:.2f} sq.ft")
        except ValueError:
            self.clear_result('result_bkd_to_sqft')
            self.show_result('result_bkd_to_sqft', "Result: Invalid input")

    def convert_sqft_to_bkd(self):
        try:
            sqft = float(self.ids.sqft_bkd.text or 0)
            b, k, d = self.sqft_to_bkd(sqft)
            self.clear_result('result_sqft_to_bkd')
            self.show_result('result_sqft_to_bkd', f"Result: {b} Bigha {k} Kattha {d} Dhur")
        except ValueError:
            self.clear_result('result_sqft_to_bkd')
            self.show_result('result_sqft_to_bkd', "Result: Invalid input")

    def convert_bkd_to_sqm(self):
        try:
            b = int(self.ids.bigha.text or 0)
            k = int(self.ids.kattha.text or 0)
            d = int(self.ids.dhur.text or 0)
            sqm = self.bkd_to_sqm(b, k, d)
            self.clear_result('result_bkd_to_sqm')
            self.show_result('result_bkd_to_sqm', f"Result: {sqm:.2f} sq.m")
        except ValueError:
            self.clear_result('result_bkd_to_sqm')
            self.show_result('result_bkd_to_sqm', "Result: Invalid input")

    def convert_sqm_to_bkd(self):
        try:
            sqm = float(self.ids.sqm_bkd.text or 0)
            b, k, d = self.sqm_to_bkd(sqm)
            self.clear_result('result_sqm_to_bkd')
            self.show_result('result_sqm_to_bkd', f"Result: {b} Bigha {k} Kattha {d} Dhur")
        except ValueError:
            self.clear_result('result_sqm_to_bkd')
            self.show_result('result_sqm_to_bkd', "Result: Invalid input")

    def convert_sqm_to_sqft(self):
        try:
            sqm = float(self.ids.sqm.text or 0)
            sqft = sqm * 10.7639
            self.clear_result('result_sqm_to_sqft')
            self.show_result('result_sqm_to_sqft', f"Result: {sqft:.2f} sq.ft")
        except ValueError:
            self.clear_result('result_sqm_to_sqft')
            self.show_result('result_sqm_to_sqft', "Result: Invalid input")

    def convert_sqft_to_sqm(self):
        try:
            sqft = float(self.ids.sqft_sqm.text or 0)
            sqm = sqft / 10.7639
            self.clear_result('result_sqft_to_sqm')
            self.show_result('result_sqft_to_sqm', f"Result: {sqm:.2f} sq.m")
        except ValueError:
            self.clear_result('result_sqft_to_sqm')
            self.show_result('result_sqft_to_sqm', "Result: Invalid input")

    def convert_only_sqm_to_sqft(self):
        self.convert_sqm_to_sqft()

    def convert_only_sqft_to_sqm(self):
        self.convert_sqft_to_sqm()

    def convert_haat_to_sqft(self):
        try:
            length = float(self.ids.haat_length.text or 0)
            breadth = float(self.ids.haat_breadth.text or 0)
            sqft = length * breadth
            self.clear_result('result_haat_to_sqft')
            self.show_result('result_haat_to_sqft', f"Result: {sqft:.2f} sq.ft")
        except ValueError:
            self.clear_result('result_haat_to_sqft')
            self.show_result('result_haat_to_sqft', "Result: Invalid input")

class LandCalculatorApp(App):
    def build(self):
        return LandConverter()

if __name__ == '__main__':
    LandCalculatorApp().run()