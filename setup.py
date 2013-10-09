from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='groundwire.blog',
      version=version,
      description="Default blog configuration for Groundwire sites.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['groundwire'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.discussion',
          'plone.formwidget.recaptcha',
          'Products.Scrawl >= 2.0b1',
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
