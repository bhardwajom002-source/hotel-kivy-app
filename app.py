from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# ---------------- LOGIN ----------------
class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=30, spacing=15)

        self.user = TextInput(hint_text="Username", multiline=False)
        self.pwd = TextInput(hint_text="Password", password=True, multiline=False)

        btn = Button(text="LOGIN", size_hint=(1, 0.3))
        btn.bind(on_press=self.login)

        layout.add_widget(Label(text="Hotel Login", font_size=22))
        layout.add_widget(self.user)
        layout.add_widget(self.pwd)
        layout.add_widget(btn)

        self.add_widget(layout)

    def login(self, instance):
        if self.user.text == "admin" and self.pwd.text == "admin":
            self.manager.current = "dashboard"


# ---------------- DASHBOARD ----------------
class Dashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        layout.add_widget(Label(text="Dashboard", font_size=24))

        btn1 = Button(text="Checkout")
        btn1.bind(on_press=lambda x: setattr(self.manager, "current", "checkout"))

        btn2 = Button(text="Bill")
        btn2.bind(on_press=lambda x: setattr(self.manager, "current", "bill"))

        btn3 = Button(text="Logout")
        btn3.bind(on_press=lambda x: setattr(self.manager, "current", "login"))

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        self.add_widget(layout)


# ---------------- CHECKOUT ----------------
class Checkout(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.customer_name = TextInput(hint_text="Customer Name", multiline=False)
        self.room_no = TextInput(hint_text="Room No", multiline=False)
        self.days = TextInput(hint_text="Days", multiline=False)

        save_btn = Button(text="Generate Bill")
        save_btn.bind(on_press=self.save_data)

        self.msg = Label(text="")

        layout.add_widget(Label(text="Checkout", font_size=22))
        layout.add_widget(self.customer_name)
        layout.add_widget(self.room_no)
        layout.add_widget(self.days)
        layout.add_widget(save_btn)
        layout.add_widget(self.msg)

        self.add_widget(layout)

    def save_data(self, instance):
        App.get_running_app().bill_data = {
            "name": self.customer_name.text,
            "room": self.room_no.text,
            "days": self.days.text
        }
        self.msg.text = "Bill Ready ✔"
        self.manager.current = "bill"


# ---------------- BILL ----------------
class Bill(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.label = Label(text="")
        self.layout.add_widget(self.label)

        back = Button(text="Back to Dashboard")
        back.bind(on_press=lambda x: setattr(self.manager, "current", "dashboard"))

        self.layout.add_widget(back)
        self.add_widget(self.layout)

    def on_enter(self):
        data = App.get_running_app().bill_data
        self.label.text = (
            f"Customer: {data['name']}\n"
            f"Room: {data['room']}\n"
            f"Days: {data['days']}"
        )


# ---------------- APP ----------------
class HotelApp(App):
    bill_data = {}

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Login(name="login"))
        sm.add_widget(Dashboard(name="dashboard"))
        sm.add_widget(Checkout(name="checkout"))
        sm.add_widget(Bill(name="bill"))
        sm.current = "login"
        return sm


if __name__ == "__main__":
    HotelApp().run()
