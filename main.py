import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

try:
    from jnius import autoclass
    Context = autoclass('android.content.Context')
    Activity = autoclass('org.kivy.android.PythonActivity').mActivity
    CameraManager = Activity.getSystemService(Context.CAMERA_SERVICE)
    CameraId = CameraManager.getCameraIdList()[0]
except:
    CameraManager = None 

class FlashlightApp(App):
    def build(self):
        self.title = "كشاف هكر ماهر"
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        title_label = Label(
            text="منصة التحكم بالفلاش - هكر ماهر", 
            font_size='22sp', 
            bold=True,
            size_hint_y=0.2
        )
        layout.add_widget(title_label)

        # زر التشغيل (الأخضر)
        btn_on = Button(
            text="تشغيل الفلاش (ON)", 
            background_color=(0.15, 0.68, 0.37, 1), 
            font_size='18sp',
            bold=True
        )
        btn_on.bind(on_press=self.turn_on_flash)
        layout.add_widget(btn_on)

        # زر الإيقاف (الأحمر)
        btn_off = Button(
            text="إيقاف الفلاش (OFF)", 
            background_color=(0.75, 0.22, 0.17, 1), 
            font_size='18sp',
            bold=True
        )
        btn_off.bind(on_press=self.turn_off_flash)
        layout.add_widget(btn_off)

        # زر الخروج
        btn_exit = Button(
            text="خروج من التطبيق", 
            background_color=(0.5, 0.5, 0.5, 1), 
            font_size='16sp'
        )
        btn_exit.bind(on_press=self.exit_app)
        layout.add_widget(btn_exit)

        return layout

    def turn_on_flash(self, instance):
        if CameraManager:
            try:
                CameraManager.setTorchMode(CameraId, True)
            except Exception as e:
                print("خطأ:", e)

    def turn_off_flash(self, instance):
        if CameraManager:
            try:
                CameraManager.setTorchMode(CameraId, False)
            except Exception as e:
                print("خطأ:", e)

    def exit_app(self, instance):
        self.turn_off_flash(None)
        App.get_running_app().stop()

if __name__ == '__main__':
    FlashlightApp().run()
