from setuptools import setup, find_packages
import os
import locale


with open('README.md') as fh:
    long_desc = fh.read()


install_requirements = []
with open('requirements.txt') as fh:
    install_requirements = fh.read().splitlines()


with open(os.path.join(os.path.dirname(__file__), 'justdeepit', '__init__.py'), encoding='utf-8') as fh:
    for line in fh:
        if line.startswith('__version__'):
            exec(line)
            break


setup(
    name        = 'JustDeepIt',
    version     = __version__,
    description = 'a GUI tool for object detection and segmentation based on deep learning',
    long_description_content_type='text/markdown',
    long_description = long_desc,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: X11 Applications',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    keywords     = 'object detection, instance segmentation',
    author       = 'Jianqiang Sun',
    author_email = 'sun@biunit.dev',
    url          = 'https://github.com/biunit/JustDeepIt',
    license      = 'MIT',
    packages     = find_packages(),
    entry_points={'console_scripts': [
                        'justdeepit=justdeepit.app.app:run_app',
                    ]},
    include_package_data = True,
    zip_safe = True,
    install_requires = install_requirements,
)

