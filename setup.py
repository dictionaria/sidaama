from setuptools import setup


setup(
    name='cldfbench_sidaama',
    py_modules=['cldfbench_sidaama'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'sidaama=cldfbench_sidaama:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pydictionaria>=2.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
