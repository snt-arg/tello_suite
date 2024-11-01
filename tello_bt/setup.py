from setuptools import find_packages, setup

package_name = "tello_bt"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="snt-arg",
    maintainer_email="snt-arg@github.com",
    description="A behavior tree for the tello suite",
    license="GPL-3.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
