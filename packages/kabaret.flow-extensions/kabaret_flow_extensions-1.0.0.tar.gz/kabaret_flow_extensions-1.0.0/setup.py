import os
import setuptools
import versioneer

readme = os.path.normpath(os.path.join(__file__, '..', 'README.md'))
with open(readme, 'r') as fh:
    long_description = fh.read()
long_description += '\n\n'
changelog = os.path.normpath(os.path.join(__file__, '..', 'CHANGELOG.md'))
with open(changelog, 'r') as fh:
    long_description += fh.read()

setuptools.setup(
    name='kabaret.flow-extensions',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Baptiste Delos, Flavio Perez, Valentin Braem, Damien "dee" Coureau, Steeve Vincent',
    author_email='baptiste@les-fees-speciales.coop, flavio@lfs.coop, valentinbraem1@gmail.com, kabaret-dev@googlegroups.com, steeve.v91@gmail.com',
    description='Kabaret extension to create and activate relations at arbitrary locations in the flow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/kabaretstudio/kabaret.flow_extensions',
    license='LGPLv3+',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
    ],
    keywords='kabaret pipeline dataflow workflow',
    install_requires=[
        'kabaret>=2.3.0rc3'
    ],
    python_requires='>=3.8',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        '': ['*.css', '*.png', '*.svg', '*.gif'],
    },

)
