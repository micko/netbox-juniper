from setuptools import find_packages, setup

setup(
    name='netbox-juniper',
    version='0.1',
    description='Juniper Networks Plugin for NetBox',
    url='https://github.com/micko/netbox-juniper',
    author='Dragan Mickovic',
    author_email='dmickovic@gmail.com',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
