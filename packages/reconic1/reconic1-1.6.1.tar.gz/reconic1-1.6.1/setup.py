from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="reconic1",
    version="1.6.1",
    author="Fatih Küçükkarakurt",
    author_email="fatihkkarakurt128@gmail.com",
    description="All-in-One Reconnaissance Tool for Penetration Testing and Bounty Hunting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fkkarakurt/reconic",
    packages=find_packages(),
    install_requires=[
        "dnspython",
        "pyfiglet",
        "requests",
        "rich",
        "python-whois",
        "beautifulsoup4",
        "Jinja2"
    ],
    entry_points={
        'console_scripts': [
            'reconic1 = reconic:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
