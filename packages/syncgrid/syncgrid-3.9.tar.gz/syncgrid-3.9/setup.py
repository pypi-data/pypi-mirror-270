from setuptools import setup

setup(name='syncgrid',
      version='3.9',
      description='syncgrid, library for distributed systems',
      packages=['syncgrid'],
      author_email='syncgrid@gmail.com',
      zip_safe=False,
      )

# twine upload -u __token__ -p pypi-AgEIcHlwaS5vcmcCJGUxN2M1OTJjLTEwMzMtNDIwYi05NDRiLTg4MDYwNTFjNTg5YwACKlszLCJlM2VkZDAzYi04YjhkLTQyMzEtOWFmNC02ODRhZmExMDhjYzUiXQAABiAF44aTAv5sUiURO2J5PEmUTIy3rMcp1Qc9eCOD7iJumw dist/*