from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
             'turtlesim_controller = my_package.turtle_controller:main',
              'add_two_ints_server = my_package.add_two_ints_server:main',
               'add_two_ints_client = my_package.add_two_ints_client:main',
               'spawn = my_package.turtle_spawner:main',
               'kill = my_package.turtle_killer:main'
        ],
    },
)
