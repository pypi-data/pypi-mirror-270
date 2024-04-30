from setuptools import setup

setup(
    name="tellibot",
    version="1.0.1",
    description="A drag and drop programming to create telegram bot",
    url="https://github.com/whoisjeeva/tellibot",
    author="Jeeva",
    author_email="support@gumify.me",
    license="MIT",
    packages=["tellibot"],
    install_requires=[
        "Flask==3.0.3",
        "peewee==3.17.3",
        "requests==2.31.0",
        "python-telegram-bot==21.1.1",
        "PyMySQL==1.1.0",
        "Flask-SocketIO==5.3.6",
    ],
    entry_points={
        "console_scripts": [
            "tellibot = tellibot.tellibot:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10'
)
