import setuptools
import re
import sys

sys.path.append("./src")
import traffic_anonymous
from traffic_anonymous.myutils import project_path
import os

package_name = "traffic_anonymous"


def curr_version():
    # 方法1：通过文件临时存储版本号
    version_str = traffic_anonymous.__version__
    return version_str


def get_version():
    # 从版本号字符串中提取三个数字并将它们转换为整数类型
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", curr_version())
    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))

    # 对三个数字进行加一操作
    patch += 1
    if patch > 9:
        patch = 0
        minor += 1
        if minor > 9:
            minor = 0
            major += 1
    new_version_str = f"{major}.{minor}.{patch}"
    return new_version_str


def upload():
    with open(os.path.join(project_path, "README.md"), "r") as fh:
        long_description = fh.read()
    with open(os.path.join(project_path, "requirements.txt")) as f:
        required = f.read().splitlines()

    setuptools.setup(
        name=package_name,
        version=get_version(),
        author="aimafan",  # 作者名称
        author_email="chongrufan@nuaa.edu.cn",  # 作者邮箱
        description="流量匿名化工具",  # 库描述
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://pypi.org/project/traffic_anonymous",  # 库的官方地址
        packages=setuptools.find_packages("src"),
        package_dir={"": "src"},
        data_files=["requirements.txt"],  # yourtools库依赖的其他库
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6",
        install_requires=required,
        entry_points={
            "console_scripts": [
                "traffic_anonymous = traffic_anonymous.cli.main:main",
            ],
        },
    )


def write_now_version():
    print("Current VERSION:", get_version())
    with open("VERSION", "w") as version_f:
        version_f.write(get_version())


def main():
    try:
        upload()
        print("Upload success , Current VERSION:", curr_version())
    except Exception as e:
        raise Exception("Upload package error", e)


if __name__ == "__main__":
    main()
