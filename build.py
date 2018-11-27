import subprocess
import argparse
import sys
import pathlib


def build_docker_image(directory, image_name, build_args=None):
    build_args = build_args or dict()
    command = " ".join(
        [
            "docker build",
            *(f"--build-arg {name}={value}" for name, value in build_args.items()),
            f"-t {image_name}",
            f"{directory}",
        ]
    )
    print(command)
    subprocess.run(command.split(), stdout=sys.stdout)


def push_docker_image(image_name):
    command = f"docker push {image_name}"
    subprocess.run(command.split(), stdout=sys.stdout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path, help="Path to 'Dockerfile' folder")
    parser.add_argument("target", type=str, help="Name of resulting image")
    parser.add_argument("build_args", nargs="+", type=str)
    params = parser.parse_known_args()[0]
    build_args = dict()
    for build_arg in params.build_args:
        name, value = build_arg.split("=")
        build_args[name] = value
    print(params)
    build_docker_image(params.path, params.target, build_args)
