from setuptools import setup, find_packages

setup(
    name='ketacli',
    version='0.15',
    packages=find_packages(),
    license='MIT',
    description='KetaDB Client',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='lvheyang',
    author_email='cuiwenzheng@ymail.com',
    url='https://xishuhq.com',
    install_requires=[
        "requests",
        "prettytable",
        "pyyaml",
        "mando",
        "argcomplete",
        "faker",
        "jinja2",
    ],
    entry_points={
        'console_scripts': [
            'ketacli=ketacli.ketacli:main',
        ],
    },
)
