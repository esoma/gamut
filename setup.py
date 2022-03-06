# gamut
from codegen import generate_math_files
# python
import os
from pathlib import Path
from subprocess import run
import sys
# setuptools
from setuptools import Command, Extension, msvc, setup

generate_math_files(Path('src/gamut/math'))


def msbuild(project):
    env = msvc.msvc14_get_vc_env('x64' if sys.maxsize > 2**32 else 'x86')
    run([
        'msbuild.exe',
        project,
        '/property:Configuration=Release'
    ], env=env, shell=True, check=True)


def make(directory):
    run(['make', '-C', directory])


class BuildBullet(Command):

    description = 'build bullet'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        build_dir = 'build/bullet3'
        os.makedirs(build_dir, exist_ok=True)
        run([
            'cmake', 'vendor/bullet3',
            '-B', build_dir,
            '-D', 'BUILD_BULLET2_DEMOS=OFF',
            '-D', 'BUILD_BULLET_ROBOTICS_EXTRA=OFF',
            '-D', 'BUILD_BULLET_ROBOTICS_GUI_EXTRA=OFF',
            '-D', 'BUILD_CLSOCKET=OFF',
            '-D', 'BUILD_CONVEX_DECOMPOSITION_EXTRA=OFF',
            '-D', 'BUILD_CPU_DEMOS=OFF',
            '-D', 'BUILD_ENET=OFF',
            '-D', 'BUILD_EXTRAS=OFF',
            '-D', 'BUILD_GIMPACTUTILS_EXTRA=OFF',
            '-D', 'BUILD_HACD_EXTRA=OFF',
            '-D', 'BUILD_INVERSE_DYNAMIC_EXTRA=OFF',
            '-D', 'BUILD_OBJ2SDF_EXTRA=OFF',
            '-D', 'BUILD_OPENGL3_DEMOS=OFF',
            '-D', 'BUILD_SERIALIZE_EXTRA=OFF',
            '-D', 'BUILD_UNIT_TESTS=OFF',
            '-D', 'CMAKE_POSITION_INDEPENDENT_CODE=ON',
            '-D', 'ENABLE_VHACD=OFF',
            '-D', 'INSTALL_CMAKE_FILES=OFF',
            '-D', 'USE_DOUBLE_PRECISION=ON',
            '-D', 'USE_GLUT=OFF',
            '-D', 'USE_GRAPHICAL_BENCHMARK=OFF',
            '-D', 'USE_MSVC_RUNTIME_LIBRARY_DLL=ON',
            '-D', 'USE_SOFT_BODY_MULTI_BODY_DYNAMICS_WORLD=OFF',
        ], check=True)
        if os.name == 'nt':
            msbuild('build/bullet3/ALL_BUILD.vcxproj')
        else:
            make('build/bullet3')


physics = Extension(
    'gamut.physics._physics',
    include_dirs=['vendor/bullet3/src'],
    library_dirs=[
        'build/bullet3/lib/Release',
    ] if os.name == 'nt' else [
        'build/bullet3/src/BulletCollision',
        'build/bullet3/src/BulletDynamics',
        'build/bullet3/src/LinearMath',
    ],
    libraries=['BulletDynamics', 'BulletCollision', 'LinearMath'],
    sources=['src/gamut/physics/_physics.cpp'],
    language='c++',
)


math = Extension(
    'gamut.math._math',
    include_dirs=['vendor/glm', 'src/gamut/math'],
    sources=['src/gamut/math/_math.cpp'],
    language='c++',
)


setup(
    cmdclass={
        "build_bullet": BuildBullet,
    },
    ext_modules=[math, physics]
)
