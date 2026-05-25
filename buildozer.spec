[app]
title = Maher Flashlight
package.name = maherflashlight
package.domain = com.maher
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius

# الصلاحيات الأساسية
android.permissions = CAMERA, FLASHLIGHT

orientation = portrait
fullscreen = 1

# تحديد إصدارات مستقرة ومجربة سحابياً لتجنب خطأ Aidl
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.skip_update = False
android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
