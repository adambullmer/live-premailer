from distutils.core import setup


setup(
    name='lpremailer',
    packages=['lpremailer'],
    version='0.1',
    description='Live premailer for jinja2 templates',
    author='turkus',
    author_email='wojciechrola@wp.pl',
    url='https://github.com/turkus/live-premailer',
    download_url='https://github.com/turkus/live-premailer/tarball/0.1',
    keywords=['live', 'browsersync', 'premailer'],
    entry_points={
        'console_scripts': [
            'lpremailer = lpremailer.main:main',
        ]
    },
    install_requires=['jinja2', 'watchdog'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
)