# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='summarize_api',
    version='0.1',
    author='Nil Portugués Calderó',
    author_email='contact@nilportugues.com',
    url='http://nilportugues.com/',
    license='BSD',
    packages=find_packages(exclude=('tests', 'docs', 'venv')),
    install_requires=[
        'virtualenv',
        'flask-restplus==0.9.2',
        'flask-restful-swagger-2==0.35',
        'Flask-SQLAlchemy==2.1',
        'summa==0.0.7'
    ],
    include_package_data=True, 
)

# EOF
