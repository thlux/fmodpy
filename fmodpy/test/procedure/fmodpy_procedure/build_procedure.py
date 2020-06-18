from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

mod_name = 'procedure'
cython_wrapper_file = 'procedure.pyx'
c_compiler_args = ['-O3']
c_linker_args = ['-lgfortran']
link_files = ['procedure.o', 'procedure_bind_c.o']

# Generate the extension module
ext_modules = [ Extension(mod_name, [cython_wrapper_file],
                          extra_compile_args=c_compiler_args,
                          extra_link_args=c_linker_args + link_files,
                          include_dirs = [numpy.get_include()])]
# Compile the '.pyx' Cython file into a '.c' file, load as an extension.
extensions = cythonize(ext_modules)
dist = setup(name=mod_name, ext_modules=extensions)