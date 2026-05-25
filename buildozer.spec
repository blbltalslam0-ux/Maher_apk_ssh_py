[app]
title = Maher Flashlight
package.name = maherflashlight
package.domain = com.maher
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius

# الصلاحيات الحساسة التي يحتاجها الأندرويد لتشغيل الفلاش
android.permissions = CAMERA, FLASHLIGHT

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
