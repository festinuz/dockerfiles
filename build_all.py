from typing import Dict
from dataclasses import dataclass

from build import build_docker_image


NAME_PREFIX = "festinuz/"


@dataclass
class ImageData:
    path: str
    name: str
    build_args: Dict[str, str]


image_datas = list()
# Add ubuntu images
for version in ["16.04"]:
    base = ImageData(path="ubuntu/base", name=f"ubuntu:{version}", VERSION=version)
    chromedriver = ImageData(
        path="ubuntu/chromedriver",
        name=f"ubuntu:{version}-chromedriver",
        PREFIX=NAME_PREFIX,
        VERSION=version,
    )
    image_datas.extend([base, chromedriver])


for image_data in image_datas:
    print(f"Building: {image_data}")
    full_image_name = NAME_PREFIX + image_data.name
    build_docker_image(image_data.path, full_image_name)
