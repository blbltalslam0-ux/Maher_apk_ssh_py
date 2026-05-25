[app]
title = Maher Flet Light
package.name = maherfletlight
package.domain = com.maher
source.dir = .
source.include_exts = py
version = 1.0

# نحدد مكتبة flet ومكتبة jnius للتحكم بالنظام
requirements = python3,flet,pyjnius

android.permissions = CAMERA, FLASHLIGHT
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 1
