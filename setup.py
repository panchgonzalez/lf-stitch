import setuptools

setuptools.setup(
    name="lfstitch",
    version="0.0.1",
    url="",
    license="",
    author="Francisco Gonzalez",
    author_email="fg@panch.io",
    description="Simple image stitcher",
    entry_points={"console_scripts": ["stitch=lfstitch.cli:stitch"]},
)
