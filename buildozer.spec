[app]
title = Maher Hacker
package.name = maherhacker
package.domain = com.maher
source.dir = .
source.include_exts = py
version = 1.0

# المتطلبات الأساسية الصافية فقط لربط الكود بنظام أندرويد
requirements = python3,pyjnius

android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 1
