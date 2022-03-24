
# python
import os
from pathlib import Path
from subprocess import run
import sys
# setuptools
from setuptools import Command, Extension, msvc, setup

coverage_compile_args = []
coverage_links_args = []
if len(sys.argv) > 1 and sys.argv[1] == '--build-with-coverage':
    if os.name == 'nt':
        print('Cannot build with coverage on windows.')
        sys.exit(1)
    coverage_compile_args = ['-fprofile-arcs', '-ftest-coverage', '-O0']
    coverage_links_args = ['-fprofile-arcs']
    sys.argv.pop(1)


def msbuild(project):
    env = msvc.msvc14_get_vc_env('x64' if sys.maxsize > 2**32 else 'x86')
    run([
        'msbuild.exe',
        project,
        '/property:Configuration=Release'
    ], env=env, shell=True, check=True)


def make(*args):
    run(['make', '-C', *args])


class GenerateMathCode(Command):

    description = 'generate math code'
    user_options = []


    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # gamut
        from codegen import generate_math_files
        generate_math_files(Path('src/gamut/math'), Path('include/gamut'))


class BuildBoost(Command):

    description = 'build boost'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        install_dir = os.path.abspath('build/boost')
        os.makedirs(install_dir, exist_ok=True)
        build_dir = 'build/boost-cmake'
        os.makedirs(build_dir, exist_ok=True)
        run([
            'cmake', 'vendor/boost',
            '-B', build_dir,
            '-D', 'BOOST_INSTALL_LAYOUT=system',
            '-D', f'CMAKE_INSTALL_PREFIX={install_dir}',
        ], check=True)
        if os.name == 'nt':
            msbuild('build/boost-cmake/INSTALL.vcxproj')
        else:
            make('build/boost-cmake', 'install')


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
            '-D', 'BUILD_BULLET3=OFF',
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


class BuildCgal(Command):

    description = 'build bullet'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        install_dir = os.path.abspath('build/cgal')
        os.makedirs(install_dir, exist_ok=True)
        build_dir = 'build/cgal-cmake'
        os.makedirs(build_dir, exist_ok=True)
        run([
            'cmake', 'vendor/cgal',
            '-B', build_dir,
            '-D', 'CMAKE_BUILD_TYPE=Release',
            '-D', f'CMAKE_INSTALL_PREFIX={install_dir}',
        ], check=True)
        if os.name == 'nt':
            msbuild('build/cgal-cmake/INSTALL.vcxproj')
        else:
            make('build/cgal-cmake', 'install')


physics = Extension(
    'gamut.physics._physics',
    include_dirs=['vendor/glm', 'vendor/bullet3/src', 'include'],
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
    extra_compile_args=coverage_compile_args,
    extra_link_args=coverage_links_args,
)


math = Extension(
    'gamut.math._math',
    libraries=[] if os.name == 'nt' else ['stdc++'],
    include_dirs=['vendor/glm', 'src/gamut/math', 'include'],
    sources=['src/gamut/math/_math.cpp'],
    language='c++11',
    extra_compile_args=coverage_compile_args +
        ([] if os.name == 'nt' else ['-std=c++11']),
    extra_link_args=coverage_links_args,
)


geometry_triangulate = Extension(
    'gamut.geometry._triangulate',
    include_dirs=[
        'vendor/glm',
        'build/cgal/include',
        'build/boost/include',
        'include'
    ],
    sources=['src/gamut/geometry/_triangulate.cpp'],
    language='c++14',
    extra_compile_args=coverage_compile_args +
        ([] if os.name == 'nt' else ['-std=c++14']),
    extra_link_args=coverage_links_args,
)


test_math_api = Extension(
    'gamut.math._test_api',
    include_dirs=['include'],
    sources=['src/gamut/math/_test_api.c'],
    language='c',
    extra_compile_args=coverage_compile_args,
    extra_link_args=coverage_links_args,
)


setup(
    cmdclass={
        "build_boost": BuildBoost,
        "build_bullet": BuildBullet,
        "build_cgal": BuildCgal,
        "codegen_math": GenerateMathCode,
    },
    ext_modules=[geometry_triangulate, math, physics, test_math_api]
)
