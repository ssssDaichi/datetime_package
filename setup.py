from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'volume_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/volume_package']),
        ('share/' + package_name, ['package.xml']),
       (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Daichi Hirose',
    maintainer_email='marumaru09030903@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'volume_talker = volume_package.volume_talker:main',
        'volume_listener = volume_package.volume_listener:main',
    ],
},



)
