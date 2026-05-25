import time
from jnius import autoclass

def run_app():
    # استدعاء واجهة الرسائل المنبثقة الصافية في نظام الأندرويد
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Toast = autoclass('android.widget.Toast')
    context = PythonActivity.mActivity

    # النص السري الخاص بك
    message = "أهلاً بكم بأول تطبيق قد تم إنشاؤه للهكر ماهر"

    # أمر إظهار الرسالة على الشاشة بخط النظام الافتراضي
    context.runOnUiThread(lambda: Toast.makeText(context, message, Toast.LENGTH_LONG).show())
    
    # انتظر 4 ثوانٍ لكي يرى المستخدم الرسالة بوضوح قبل إغلاق التطبيق
    time.sleep(4)

if __name__ == "__main__":
    run_app()
