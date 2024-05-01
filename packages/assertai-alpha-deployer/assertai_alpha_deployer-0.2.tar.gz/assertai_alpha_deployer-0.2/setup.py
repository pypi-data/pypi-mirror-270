from setuptools import setup

setup(
    name='assertai_alpha_deployer',
    version='0.2',
    packages=['assertai_alpha_deployer'],
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'assertai-alpha-deployer=assertai_alpha_deployer.__main__:main',
        ],
    },
)
