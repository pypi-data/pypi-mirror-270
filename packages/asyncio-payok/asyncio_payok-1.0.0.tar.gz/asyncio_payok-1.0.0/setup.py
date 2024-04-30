from setuptools import setup, find_packages

setup(
	name='asyncio_payok',
	version='1.0.0',
	author='Abracadabra',
	author_email='stopcrybby@gmail.com',
	description='Asyncio client for PayOk API',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/slimeless/asycncio-payok',
	packages=find_packages(),
	install_requires=[
		'aiohttp',
		'pydantic',

	],
	python_requires='>=3.6',
)
