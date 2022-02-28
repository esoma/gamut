# setuptools
from setuptools import Extension, find_packages, setup

# CMAKE_POSITION_INDEPENDENT_CODE=ON
# USE_DOUBLE_PRECISION=ON

physics = Extension(
    'gamut.physics._physics',
    include_dirs=[
        r'C:\Users\erik\Documents\code\bullet3\src',
        #r'/home/erik/bullet3/src',
    ],
    library_dirs=[
        r'C:\Users\erik\Documents\code\bullet3\build\lib\Release',
        #r'/home/erik/bullet3/src/BulletCollision/',
        #r'/home/erik/bullet3/src/BulletDynamics/',
        #r'/home/erik/bullet3/src/LinearMath/',
    ],
    libraries=['BulletDynamics', 'BulletCollision', 'LinearMath'],
    sources=[
        'src/gamut/physics/_physics.cpp',
    ],
    #extra_compile_args=['/Zi'],
    #extra_link_args=['/DEBUG'],
    language='c++',
)

setup(ext_modules=[physics])
