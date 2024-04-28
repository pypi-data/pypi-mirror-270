from setuptools import setup, find_packages

import os


REQUIREMENTS = [
    'Django==3.2.16',
    'djangorestframework==3.15.1',
    'drf_yasg==1.21.7',
    'django-cors-headers==4.3.1'
]

if __name__ == '__main__':
    setup(
        author="Maxim Ignatov",
        author_email="ignatov.mack@gmail.com",
        name="cpu_info",
        url='https://github.com/Maxon57/CPU',
        description="Getting cpu information",
        packages=find_packages(),
        version=os.getenv('PACKAGE_VERSION', '0.1.1'),
        include_package_data=True,
        install_requires=REQUIREMENTS
    )
