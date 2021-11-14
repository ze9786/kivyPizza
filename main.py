from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.widget import Widget

Builder.load_file("main.kv")


class PizzaBoxLayout(BoxLayout):
    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate()

    def populate(self):
        rows = [("asdfaadsf", "$100"), ("qewr", "$1020"), ("zcxv", "$500")]
        for row in rows:
            for col in row:
                self.data_items.append(col)
        print(self.data_items)

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {
            'name.text': value or 'default value', 'value': 'unknown'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['name.text'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)


class MenuScreen(Screen):
    def gotoPizza(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'pizza'


class PizzaScreen(Screen):
    def goBack(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'

    def goPreview(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'preview'


class PreviewBoxLayout(BoxLayout):
    data_items = ListProperty([])
    amount = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.populate()

    def populate(self):
        rows = [("asdfaadsf", 1, 100), ("qewr", 2, 1020), ("zcxv", 3, 500)]
        for row in rows:
            for col in row:
                self.data_items.append(col)
        print(self.data_items)
        total = 0

        for i in range(len(self.data_items)):
            qty = 0
            price = 0
            # if (i+1) % 3 == 0:
            #     qty = self.data_items[i]
            # elif (i-2) % 3 == 0:
            #     price = self.data_items[i]
            total += qty * price

        self.amount = str(total)

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['name.text'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {
            'name.text': value or 'default value', 'value': 'unknown'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['name.text'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)


class PreviewScreen(Screen):
    def goBack(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'

    def confirmBtnOnPressed(self):
        return


class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_preview = ObjectProperty(None)


class TestApp(App):
    def build(self):
        sm = Manager(transition=SlideTransition())
        return sm
        # return Test()


if __name__ == '__main__':
    TestApp().run()
