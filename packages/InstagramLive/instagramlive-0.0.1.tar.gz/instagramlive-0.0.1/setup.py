import setuptools

# PyPi upload Command
# rm -r dist ; python setup.py sdist ; python -m twine upload dist/*

manifest: dict = {
    "name": "InstagramLive",
    "license": "MIT",
    "author": "Isaac Kogan",
    "version": "0.0.1",
    "email": "info@isaackogan.com"
}

if __name__ == '__main__':
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name=manifest["name"],
        packages=setuptools.find_packages(),
        version=manifest["version"],
        license=manifest["license"],
        description="Instagram Live Python Client",
        author=manifest["author"],
        author_email=manifest["email"],
        url="https://github.com/isaackogan/InstagramLive",
        long_description=long_description,
        long_description_content_type="text/markdown",
        # download_url=f"https://github.com/isaackogan/TikTokLive/releases/tag/v{manifest['version']}",
        keywords=["instagram", "instagram live", "python3", "api", "ig", "ig live"],
        install_requires=[
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ]
    )
