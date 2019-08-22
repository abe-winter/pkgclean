from distutils.core import setup

setup(name='pkgclean',
  version='0.0.1',
  description='find (or delete) disposable package directories to save space',
  author='Abe Winter',
  author_email='awinter.public@gmail.com',
  url='https://github.com/abe-winter/deltree',
  py_modules=['pkgclean'],
  entry_points={'console_scripts':['pkgclean=pkgclean:main']},
)
