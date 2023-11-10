from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*')),
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
            'kenneth = my_package.kenneth:main',
            'publisher = my_package.publisher:main',
            'subscriber = my_package.subscriber:main',
            'num_pub = my_package.number_publisher:main',
            'num_count = my_package.number_counter:main'
        ],
    },
)
