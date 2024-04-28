from setuptools import setup, find_packages

setup(name='rahul_library',
      version='0.01',
      description='operation & greeting library',
      packages=find_packages('rahul-library', exclude=['test']),
      author_email='codewithrahulnikam@gmail.com',
      zip_safe=False)

