from setuptools import setup, find_packages

setup(
    name='STAIR-tools',  
    packages=find_packages(),
    package_data={
        'STAIR-tools': ['/ABAanno/ccfv3/*.nrrd', '/ABAanno/*.csv', '/ABAanno/*.pkl'],
    },
    version='1.1.8',
    description='Spatial Transcriptomic Alignment, Integration, and de novo 3D Reconstruction',
    author='yuanyuanyu',
    license='MIT',
    URL='https://github.com/yuyuanyuana/STAIR'
)