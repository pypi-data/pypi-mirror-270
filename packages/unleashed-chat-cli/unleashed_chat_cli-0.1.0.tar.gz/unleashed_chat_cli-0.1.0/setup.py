from setuptools import setup, find_packages

setup(
    name='unleashed-chat-cli',
    version='0.1.0',
    author="Reece Hunter",
    description="A simple CLI wrapper for Unleashed.chat's chatbot service.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/reecehunter/unleashed-chat-cli",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'unleashed-chat=unleashed_chat_cli.main:main',
        ],
    },
)