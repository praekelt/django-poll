from setuptools import setup, find_packages

setup(
    name='django-poll',
    version='dev',
    description='Django poll app.',
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='https://github.com/praekelt/django-poll',
    packages = find_packages(),
    include_package_data=True,
)

