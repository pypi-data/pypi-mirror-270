from setuptools import setup, find_packages

# Membaca isi dari requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='geramcals',
    version='1.0',
    packages=find_packages(),
    description='Seratus Persen Clone Pytgcalls',
    author='pyrogeram',
    author_email='pyrogeram@gmail.com',
    url='https://t.me/pypyrogramcalls',  # Ganti dengan URL proyek Anda
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
)

