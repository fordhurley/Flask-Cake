"""
Flask-Cake
----------

Flask extension to execute Cake on filesystem events.
"""
from setuptools import setup


setup(
    name='Flask-Cake',
    version='0.1',
    url='http://github.com/rsenk330/Flask-Cake',
    license='BSD',
    author='Ryan Senkbeil',
    author_email='rsenk330@gmail.com',
    description='Flask extension to execute Cake on filesystem events.',
    long_description=__doc__,
    packages=['flask_cake'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'watchdog'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
