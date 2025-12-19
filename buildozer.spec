[app]

# App title
title = HotelApp

# Package name
package.name = hotelapp

# Package domain (reverse domain)
package.domain = org.bhardwaj

# Source code directory
source.dir = .

# Main file
source.main = main.py

# App version (MANDATORY – AIDL error se pehle ka root fix)
version = 1.0

# List of requirements
requirements = python3,kivy

# Screen orientation
orientation = portrait

# Android API level
android.api = 33

# Android minimum API
android.minapi = 21

# Android NDK version (GitHub Actions compatible)
android.ndk = 25b

# Android permissions
android.permissions = INTERNET

# Allow internet
android.allow_backup = True

# Fullscreen mode
fullscreen = 0

# Log level
log_level = 2

# ===============================
# 🔴 VERY IMPORTANT (AIDL FIX)
# ===============================

# GitHub Actions Android SDK path
android.sdk_path = /home/runner/android-sdk

# GitHub Actions Android NDK path
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# ===============================
# Build options
# ===============================

# Enable debug build
android.debug = 1

# Architecture
android.arch = armeabi-v7a,arm64-v8a

# Use gradle
android.gradle_dependencies = 

# Clean build
android.clean_build = 1

# ===============================
# Exclude files
# ===============================
source.exclude_dirs = tests,bin,__pycache__
source.exclude_patterns = *.pyc,*.pyo,*.swp

