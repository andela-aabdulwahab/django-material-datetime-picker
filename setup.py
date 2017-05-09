from setuptools import setup

setup(
    name='django-material-datetime-picker',
    version='0.0.1',
    author='Abdulmalik Abdulwahab',
    author_email='malik.adeyi@gmail.com',
    description='Based on md-date-time-picker an implementaion of the the material picker component',
    packages=['django_material_datetime_picker'],
    include_package_data=True,
    license='MIT',
    install_requires=['django'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

# python setup.py develop to pip install a development Environment
