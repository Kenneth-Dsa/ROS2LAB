from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'lab4'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
                 (os.path.join('share', package_name), glob('urdf/*')),
           (os.path.join('share', package_name), glob('launch/*'))
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
            'controller = lab4.move_robot:main',
            'wall_follower = lab4.wall_follower:main'
        ],
    },
)
