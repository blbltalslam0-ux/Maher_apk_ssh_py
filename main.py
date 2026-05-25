import flet as ft

def main(page: ft.Page):
    page.title = "Maher Flashlight"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # دالة التحكم بالزر والكشاف
    def toggle_flashlight(e):
        if btn.text == "تشغيل الكشاف":
            btn.text = "إطفاء الكشاف"
            btn.bgcolor = ft.colors.RED
            # هنا سنضع كود تشغيل الفلاش للأندرويد لاحقاً
        else:
            btn.text = "تشغيل الكشاف"
            btn.bgcolor = ft.colors.GREEN
        page.update()

    # إنشاء زر كبير واحترافي
    btn = ft.ElevatedButton(
        text="تشغيل الكشاف",
        bgcolor=ft.colors.GREEN,
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        width=250,
        height=60,
        on_click=toggle_flashlight
    )

    page.add(btn)

# تشغيل التطبيق
ft.app(target=main)
