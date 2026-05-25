[app]
title = Maher Light
package.name = maherlight
package.domain = com.maher
source.dir = .
source.include_exts = py
version = 1.0

# المتطلبات الأساسية فقط دون أي إضافات جرافيكس ثقيلة
requirements = python3,kivy==2.2.1,pyjnius

android.permissions = CAMERA, FLASHLIGHT
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 1
warn_on_root = 1
