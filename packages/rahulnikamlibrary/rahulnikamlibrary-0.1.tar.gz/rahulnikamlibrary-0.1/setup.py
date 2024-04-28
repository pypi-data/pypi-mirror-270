from setuptools import setup, find_packages

setup(name='rahulnikamlibrary',
      version='0.01',
      description='operation & greeting library',
      packages=find_packages('rahulnikamlibrary', exclude=['test']),
      author_email='codewithrahulnikam@gmail.com',
      zip_safe=False)

