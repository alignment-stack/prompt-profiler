import os
from setuptools import setup, find_packages

if os.path.exists("requirements.txt"):
    with open("requirements.txt", encoding="utf-8") as f:
        requirements = [
            req.strip()
            for req in f
            if req.strip() and not req.startswith("#")
        ]
else:
    requirements = [] 

if os.path.exists("README.md"):
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "A tool for profiling prompts."

setup(
    name="prompt-profiler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "prompt-profiler=prompt_profiler.main:main",
        ],
    },
)

