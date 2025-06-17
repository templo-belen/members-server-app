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
        "pydantic==2.11.3",
        "bcrypt==4.0.1",
        "pydantic-settings==2.9.1",
    ],
    extras_require={
        "dev": [
            "iniconfig==2.1.0",
            "packaging==25.0",
            "pluggy==1.6.0",
            "pytest==8.4.0",
            "black==25.1.0",
            "mypy-extensions==1.1.0",
            "pathspec==0.12.1",
            "ruff==0.11.13",
            "isort==5.10.1",
            "pre-commit==4.2.0",
        ]
    },
)
