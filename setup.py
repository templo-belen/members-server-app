from setuptools import find_packages, setup

setup(
    name="members_server_app",
    packages=find_packages(exclude=["members_server_app_tests"]),
    install_requires=[
        "SQLAlchemy==2.0.40",
        "fastapi[standard]==0.115.12",
        "python-dotenv==1.1.0",
        "python-jose==3.4.0",
        "passlib==1.7.4",
        "psycopg2-binary==2.9.10",
        "typing==3.7.4.3",
        "python-dotenv==1.1.0",
        "pydantic==2.11.3",
        "bcrypt==4.0.1",
        "pydantic-settings==2.9.1",
    ],
    extras_require={"dev": ["pytest"]},
)
