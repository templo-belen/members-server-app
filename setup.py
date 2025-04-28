from setuptools import find_packages, setup

setup(
    name="members_server_app",
    packages=find_packages(exclude=["members_server_app_tests"]),
    install_requires=[
        "SQLAlchemy==2.0.40",
        "fastapi[standard]==0.115.12"
    ],
    extras_require={"dev": ["pytest"]},
)
