from struct import pack
from setuptools import setup, find_packages

setup(
    name='mensajes-caraldana2024',
    version='6.0',
    description='un paquete para saludar y despedir',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Héctor Costa Guzmán',
    author_email='hola@hektor.dev',
    url='https://www.hektor.dev',
    license_files=['LICENSE'],
    packages= find_packages(),
    scripts=[],
    test_suite='tests',
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12',
        'Topic :: Utilities'
    ]

)




