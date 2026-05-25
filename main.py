from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from jnius import autoclass

class FlashlightApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        
        # زر التحكم بالكشاف
        self.btn = Button(
            text="تشغيل الكشاف",
            font_size='24sp',
            background_color=(0, 1, 0, 1) # لون أخضر
        )
        self.btn.bind(on_press=self.toggle_flashlight)
        
        layout.add_widget(self.btn)
        return layout

    def toggle_flashlight(self, instance):
        # هنا سيتم ربط كود الفلاش الصافي لاحقاً
        if self.btn.text == "تشغيل الكشاف":
            self.btn.text = "إطفاء الكشاف"
            self.btn.background_color = (1, 0, 0, 1) # لون أحمر
        else:
            self.btn.text = "تشغيل الكشاف"
            self.btn.background_color = (0, 1, 0, 1) # لون أخضر

if __name__ == '__main__':
    FlashlightApp().run()
