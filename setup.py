from setuptools import setup, find_namespace_packages

setup(name='cool_app',
      version='0.0.2',
      author='GoIT_students',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['greeting = my_project.main:greeting',
                                        'greeting_by_name = my_project.main:greeting_name']})