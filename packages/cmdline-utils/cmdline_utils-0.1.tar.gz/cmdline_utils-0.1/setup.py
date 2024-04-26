from setuptools import setup, find_packages

setup(
    name="cmdline_utils",
    version = 0.1,
    packages=find_packages(),
    install_requires=[
        "groq",  
    ],
    entry_points={
        'console_scripts': [
            'clu=cmdline_utils.clu:main',
        ],
    },
    keywords=['python', 'groq', 'llama3 70b'],
    python_requires='>=3.8',
    author="Sunil Aleti",
    author_email="iam@sunilaleti.dev",
    description="A CLI tool for helping commands with Groq",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aletisunil/cmdline_utils',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)