from typing import Dict
from dataclasses import dataclass

from build import build_docker_image, push_docker_image


NAME_PREFIX = "festinuz/"


@dataclass
class ImageData:
    path: str
    name: str
    build_args: Dict[str, str]


image_datas = list()
# Add ubuntu images
for version in ["16.04"]:
    base = ImageData(
        path="ubuntu/base", name=f"ubuntu:{version}", build_args=dict(VERSION=version)
    )
    chromedriver = ImageData(
        path="ubuntu/chromedriver",
        name=f"ubuntu:{version}-chromedriver",
        build_args=dict(PREFIX=NAME_PREFIX, VERSION=version),
    )
    python_version = "3.6.6"
    python = ImageData(
        path="ubuntu/python",
        name=f"ubuntu:{version}-python{python_version}",
        build_args=dict(UBUNTU_VERSION=version, PYTHON_VERSION=python_version),
    )
    pyinstaller = ImageData(
        path="ubuntu/pyinstaller",
        name=f"ubuntu:{version}-pyinstaller{python_version}",
        build_args=dict(
            PREFIX=NAME_PREFIX, UBUNTU_VERSION=version, PYTHON_VERSION=python_version
        ),
    )
    image_datas.extend([base, chromedriver, python, pyinstaller])


for image_data in image_datas:
    print(f"Building: {image_data}")
    full_image_name = NAME_PREFIX + image_data.name
    build_docker_image(image_data.path, full_image_name, image_data.build_args)
    push_docker_image(full_image_name)
