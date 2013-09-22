import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-site-basics',
    version=__import__('site_basics').__version__,
    author='Evgeny Demchenko',
    author_email='little_pea@list.ru',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/littlepea/django-site-basics',
    license='BSD',
    description=u' '.join(__import__('site_basics').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        "Django>=1.4",
        "django-favicon",
        "django-robots-txt",
        "django-sitemetrics==0.2",
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
)
