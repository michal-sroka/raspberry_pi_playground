# Copyright Michal Sroka

import setuptools

setuptools.setup(
    name="raspberry_pi_playground",
    version="1.0.0",
    license="MIT",
    author="Michal Sroka",
    author_email="msmisiu@gmail.com",
    description="Provides tools to get measurements from Raspberry Pi sensors and store them in Azure.",
    url="michalsroka.com",
    packages=setuptools.find_packages(exclude=("test",)),
    # install_requires=_requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT'
    ],
    keywords=['Raspberry Pi'],
    include_package_data=True,
    zip_safe=False
)
