# Privacy Protection

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub](https://img.shields.io/github/license/mmphego/privacy_protection.svg)](LICENSE)
[![Build Status](https://img.shields.io/travis/mmphego/privacy_protection.svg)](https://travis-ci.com/mmphego/privacy_protection)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43713e0b78f547e8912ff05c9350cffb)](https://app.codacy.com/app/mmphego/privacy_protection?utm_source=github.com&utm_medium=referral&utm_content=mmphego/privacy_protection&utm_campaign=Badge_Grade_Dashboard)
[![Python](https://img.shields.io/badge/Python-3.6%2B-red.svg)](https://www.python.org/downloads/)
[![Donate](https://img.shields.io/badge/Donate-%24-green.svg)](https://paypal.me/mmphego)

Detect human faces in the image and for the sake of privacy, anonymize the images by blurring people's faces in the image automatically.

# Usage

```bash
docker run --rm -ti \
--volume "$PWD":/app \
--env DISPLAY=$DISPLAY \
--volume=$HOME/.Xauthority:/root/.Xauthority \
--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--device /dev/video0 \
mmphego/intel-openvino \
bash -c "\
    source /opt/intel/openvino/bin/setupvars.sh && \
    python main.py -i blm.jpg
    "
```

## Example

Input image:
![](./blm.jpg)

Output image:
![](./Blurred_Faces.jpg)


# Feedback

Feel free to fork it or send me PR to improve it.

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [mmphego/cookiecutter-python-package](https://github.com/mmphego/cookiecutter-python-package) project template.
