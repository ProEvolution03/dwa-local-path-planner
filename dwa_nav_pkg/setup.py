from setuptools import find_packages, setup

package_name = 'dwa_nav_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),  # Ensure resource folder exists
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aakashsivakumar',
    maintainer_email='aakashiyer03@gmail.com',
    description='A custom Dynamic Window Approach (DWA) planner for ROS2 TurtleBot3',
    license='MIT',  # Change this if necessary
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'run_dwa = dwa_nav_pkg.dwa_planner:main',
        ],
    },
)
