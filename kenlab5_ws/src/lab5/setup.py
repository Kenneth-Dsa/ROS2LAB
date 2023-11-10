from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'lab5'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*')),
        (os.path.join('share',package_name),glob('urdf/*')),
        (os.path.join('share',package_name),glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kennethdsa',
    maintainer_email='kennethdsa@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control=lab5.controller:main',
            'final_destination=lab5.final_destination:main'
        ],
    },
)
