from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        # Remove the script_manager.py file after installation
        script_manager_path = os.path.join(self.install_lib, 'assertai_alpha_deployer', 'script_manager.py')
        if os.path.exists(script_manager_path):
            os.remove(script_manager_path)

setup(
    name='assertai_alpha_deployer',
    version='4.7',
    packages=find_packages(),
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'assertai-alpha-deployer=assertai_alpha_deployer.__main__:main',
        ],
    },
    author='Rajesh Roy',
    author_email='rajeshroy402@gmail.com',
    description='A package to deploy python codes on bare-metal',
    long_description='A longer description of your package, can be the content of your README file',
    url='https://www.linkedin.com/in/rajeshroy402',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
