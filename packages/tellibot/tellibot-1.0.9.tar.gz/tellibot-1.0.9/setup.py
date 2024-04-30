from setuptools import setup, find_packages


setup(
    name="tellibot",
    version="1.0.9",
    description="A drag and drop programming to create telegram bot",
    url="https://github.com/whoisjeeva/tellibot",
    author="Jeeva",
    author_email="support@gumify.me",
    license="MIT",
    packages=find_packages(),
    package_data={'tellibot': ["tellibot/templates", "tellibot/static"]},
    include_package_data=True,
    install_requires=[
        "anyio==4.3.0",
        "bidict==0.23.1",
        "blinker==1.8.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "docutils==0.21.2",
        "Flask==3.0.3",
        "Flask-SocketIO==5.3.6",
        "h11==0.14.0",
        "httpcore==1.0.5",
        "httpx==0.27.0",
        "idna==3.7",
        "importlib_metadata==7.1.0",
        "itsdangerous==2.2.0",
        "jaraco.classes==3.4.0",
        "jaraco.context==5.3.0",
        "jaraco.functools==4.0.1",
        "Jinja2==3.1.3",
        "keyring==25.2.0",
        "markdown-it-py==3.0.0",
        "MarkupSafe==2.1.5",
        "mdurl==0.1.2",
        "more-itertools==10.2.0",
        "nh3==0.2.17",
        "peewee==3.17.3",
        "pkginfo==1.10.0",
        "Pygments==2.17.2",
        "PyMySQL==1.1.0",
        "python-engineio==4.9.0",
        "python-socketio==5.11.2",
        "python-telegram-bot==21.1.1",
        "pywin32-ctypes==0.2.2",
        "readme_renderer==43.0",
        "requests==2.31.0",
        "requests-toolbelt==1.0.0",
        "rfc3986==2.0.0",
        "rich==13.7.1",
        "simple-websocket==1.0.0",
        "sniffio==1.3.1"
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
