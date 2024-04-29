# 🚀 Ubo App

[![image](https://img.shields.io/pypi/v/ubo-app.svg)](https://pypi.python.org/pypi/ubo-app)
[![image](https://img.shields.io/pypi/l/ubo-app.svg)](https://github.com/ubopod/ubo-app/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/ubo-app.svg)](https://pypi.python.org/pypi/ubo-app)
[![Actions status](https://github.com/ubopod/ubo-app/workflows/CI/CD/badge.svg)](https://github.com/ubopod/ubo-app/actions)
[![codecov](https://codecov.io/gh/ubopod/ubo-app/graph/badge.svg?token=KUI1KRDDY0)](https://codecov.io/gh/ubopod/ubo-app)

## 🌟 Overview

Ubo App is a Python application for managing Raspberry Pi utilities and Ubo-specific
features.

<img width="550" alt="Ubo ai pod photo" src="https://github.com/ubopod/ubo-app/assets/94014876/9438ab51-9b40-46b8-a656-80b8fcb72bc3">

Example screenshots:

<img width="200" alt="Ubo ai pod photo" src="https://github.com/ubopod/ubo-app/assets/94014876/899d32e4-ef8e-4849-a967-1e21ad12297a">

## 🚧 Disclaimer

Be aware that at the moment, Ubo app sends crash reports to Sentry. Soon we will
limit this to beta versions only.

## ⚙️ Notable Features

- Headless WiFi on-boarding with QR code
- Easy headless remote access with SSH and VS Code tunnel
- Install and run Docker apps headlessly
- Access and control basic RPi utilities and settings

## 📋 Requirements

Ubo app is developed to run on Raspberry Pi 4 and 5. The experience is optimized around Ubo Pod which offers

- a minimal LCD display and GUI with a keypad
- stereo microphone and speakers,
- camera
- LED ring
- sensors

The app functions even if some of these hardware elements are not provided, however some of the features that rely on these hardware components may not function. For example, WiFi onboarding with QR code requires a camera onboard.

## 📦 Installation

### Pre-packaged image

Ubo Pod ships with a pre-flashed MicroSD card that has the app installed on it by default.

If you don't have it, or you just want to set up a fresh device, then:

1. download one of the images from the release section
2. Use Raspberry Pi Images and choose `custom image` to provide the download image file.
3. Write to the image
4. Use the image to boot your Ubo Pod or Raspberry Pi

This is the fastest, easiest, and recommended way to get started with Ubo App.

### Install on existing OS

If you want to install the image on an existing operating system, then read on. Otherwise, skip this section.

---

⚠️ **Executing scripts directly from the internet with root privileges poses a significant
security risk. It's generally a good practice to ensure you understand the script's
content before running it. You can check the content of this particular script
[here](https://raw.githubusercontent.com/ubopod/ubo-app/main/ubo_app/system/install.sh)
before running it.**

---

To install ubo, run this command in a terminal shell:

```bash
curl -sSL https://raw.githubusercontent.com/ubopod/ubo-app/main/ubo_app/system/install.sh\
  | sudo bash
```

If you want to install docker service and configure ubo to be able to use it run
this:

```bash
curl -sSL https://raw.githubusercontent.com/ubopod/ubo-app/main/ubo_app/system/install.sh\
  | sudo WITH_DOCKER=true bash
```

To allow the installer to install the latest alpha version of ubo run this:

```bash
curl -sSL https://raw.githubusercontent.com/ubopod/ubo-app/main/ubo_app/system/install.sh\
  | sudo ALPHA=true bash
# or
curl -sSL https://raw.githubusercontent.com/ubopod/ubo-app/main/ubo_app/system/install.sh\
  | sudo ALPHA=true WITH_DOCKER=true bash
```

Note that as part of the installation process, these debian packages are installed:

- git
- i2c-tools
- libcap-dev
- libegl1
- libgl1
- libmtdev1
- libzbar0
- python3-alsaaudio
- python3-dev
- python3-gpiozero
- python3-libcamera
- python3-picamera2
- python3-pip
- python3-pyaudio
- python3-virtualenv

Also be aware that ubo-app only installs in `/opt/ubo` and it is not customizable
at the moment.

## 🤝 Contributing

Contributions following Python best practices are welcome.

### ℹ️️ Conventions

- Use `UBO_` prefix for environment variables.
- Use `ubo:` prefix for notification ids used in ubo core and `<service_name>:` prefix
  for notification ids used in services.
- Use `ubo:` prefix for icon ids used in ubo core and `<service_name>:` prefix for
  icon ids used in services.

### Development

#### QR code

In development environment, the camera is probably not working as it is relying,
on `picamera2`, so it may become challenging to test the flows relying on QR code
input.

To address this, the `qrcode_input` method, in not-RPi environments, will try to
get its input from `/tmp/qrcode_input.txt`. So, whenever you encounter a QR code
input, you can write the content of the QR code in that file and the application
will read it from there and continue the flow.

## 🔒 License

This project is released under the Apache-2.0 License. See the [LICENSE](./LICENSE)
file for more details.
