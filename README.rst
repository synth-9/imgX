====
IMGX
====

.. image:: https://img.shields.io/pypi/v/imgx.svg
        :target: https://pypi.python.org/pypi/imgx

.. image:: https://img.shields.io/travis/M-Farag/imgx.svg
        :target: https://travis-ci.com/M-Farag/imgx

.. image:: https://readthedocs.org/projects/imgx/badge/?version=latest
        :target: https://imgx.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

IMGX is a powerful, easy-to-use image processing package developed by Synth9, designed to help photographers and organizations efficiently manage and organize large image libraries across various storage devices.

* Free software: MIT license
* Documentation: https://imgx.readthedocs.io.

Features
--------

IMGX currently offers the following functionalities:

- **Directory Flattening**: Simplify your folder structure by flattening one level of subdirectories, moving all image files into the parent directory. This feature helps in consolidating scattered images into one location, making them easier to access and manage.

- **Metadata Extraction and Recording**: Automatically extract metadata from images and write this information into a file. This feature aids in cataloging and maintaining essential details about each image, such as the file size, image name, and path.

How to Use
----------

1. **Installation**:

   Install IMGX using pip:

   .. code-block:: bash

       pip install imgx

2. **Flattening Directories via CLI**:

   To flatten directories using the command line, run:

   .. code-block:: bash

       imgx flat /path/to/your/directory

   This command will flatten the directory structure at the specified path, moving all images to the parent directory.

3. **Extracting and Recording Metadata via CLI**:

   To extract metadata and write it to a file using the command line, run:

   .. code-block:: bash

       imgx read /path/to/your/directory

   This command will read the metadata from all images in the specified directory and write the information to a file in the same directory.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
