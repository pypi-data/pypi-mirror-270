from distutils.core import setup

setup(
    name="TwitchPy",
    packages=["twitchpy"],
    version="1.2.0",
    license="GPL-3.0",
    description="TwitchPy is a Python package for using the Twitch's API and create bots for interacting with their IRC chats.",
    author="DaCasBe",
    author_email="dacasbe97@gmail.com",
    url="https://github.com/DaCasBe",
    download_url="https://github.com/DaCasBe/TwitchPy/archive/refs/tags/v1.2.0.tar.gz",
    install_requires=["requests"],
)
