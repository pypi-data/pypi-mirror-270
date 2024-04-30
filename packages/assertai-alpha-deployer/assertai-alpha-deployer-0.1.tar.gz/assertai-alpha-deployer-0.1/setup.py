from setuptools import setup, find_packages

setup(
    name='assertai-alpha-deployer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'assertai-alpha-deployer=script_manager:main',
        ],
    },
)
