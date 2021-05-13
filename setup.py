import setuptools

setuptools.setup(
    name = 'boundary-layer-mycompany-plugin',
    version='0.0.1',
    author = 'Somebody',
    author_email = 'somebody@email.com',
    description = 'Company-specific configuration and code for boundary-layer',
    packages = setuptools.find_packages(),
    package_data = {
        'boundary_layer_mycompany_plugin': [
            'config/generators/*.yaml',
            'config/operators/*.yaml',
            'config/resources/*.yaml',
            'config/subdags/*.yaml',
        ]
    },
    install_requires = [
        'boundary-layer>=1.7.9,<1.10',
    ],
    extras_require = {
        'test': [
            'pytest==3.2.3',
        ],
    },
    entry_points = {
        'boundary_layer_plugins': [
                'mycompany=boundary_layer_mycompany_plugin.plugin:MyCompanyPlugin',
            ]
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    zip_safe = False,
    python_requires='>=3.6',
    keywords = 'airflow',
)
