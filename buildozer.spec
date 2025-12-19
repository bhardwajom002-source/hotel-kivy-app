[app]

# ===============================
# Basic App Info
# ===============================

title = HotelApp
package.name = hotelapp
package.domain = org.bhardwaj

# App version (MANDATORY)
version = 1.0

# Source files
source.dir = .
source.main = main.py

# Files to exclude
source.exclude_dirs = tests, bin, __pycache__
source.exclude_patterns = *.pyc, *.pyo, *.swp

# ===============================
# Requirements
# ===============================

requirements = python3,kivy

# Orientation
orientation = portrait

# Fullscreen (0 = false, 1 = true)
fullscreen = 0

# Log level
log_level = 2

# ===============================
# Android Configuration
# ===============================

# Target Android API
android.api = 33
android.minapi = 21

# NDK version (GitHub Actions compatible)
android.ndk = 25b

# CPU Architectures
android.arch = arm64-v8a,armeabi-v7a

# Permissions
android.permissions = INTERNET

# ===============================
# SDK / NDK PATH FIX (IMPORTANT)
# ===============================

# These paths are for GitHub Actions runner
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# ===============================
# Build Options
# ===============================

# Use Gradle
android.gradle = True

# Debug build
android.debug = 1

# Clean build every time
android.clean_build = 1
