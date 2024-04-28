omf
***

.. image:: https://img.shields.io/pypi/v/mira-omf.svg
    :target: https://pypi.python.org/pypi/mira-omf
    :alt: Latest PyPI version

.. image:: https://readthedocs.org/projects/omf/badge/?version=stable
    :target: http://omf.readthedocs.io/en/stable/
    :alt: Documentation

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/MiraGeoscience/omf/blob/main/LICENSE
    :alt: MIT license

.. image:: https://github.com/MiraGeoscience/omf/actions/workflows/pytest-windows.yml/badge.svg
    :target: https://github.com/MiraGeoscience/omf/actions/workflows/pytest-windows.yml
    :alt: pytest


Version: 3.2.0

API library for Open Mining Format, a new standard for mining data backed by
the `Global Mining Standards & Guidelines Group <https://gmggroup.org/>`_.


.. warning::

    This is a fork created by Mira Geoscience for interoperability with the
    geoh5 file format.

Why?
----

An open-source serialization format and API library to support data interchange
across the entire mining community.

Scope
-----

This library provides an abstracted object-based interface to the underlying
OMF serialization format, which enables rapid development of the interface while
allowing for future changes under the hood.

Goals
-----

- The goal of Open Mining Format is to standardize data formats across the
  mining community and promote collaboration
- The goal of the API library is to provide a well-documented, object-based
  interface for serializing OMF files

Alternatives
------------

OMF is intended to supplement the many alternative closed-source file formats
used in the mining community.

Connections
-----------

This library makes use of the `properties <https://github.com/seequent/properties>`_
open-source project, which is designed and publicly supported by
`Seequent <https://seequent.com>`_.

Connection to the geoh5 format makes use of `geoh5py <https://geoh5py.readthedocs.io/>`_
publicly supported by `Mira Geoscience <https://mirageoscience.com/>`_

Installation
------------

To install the repository, ensure that you have
`pip installed <https://pip.pypa.io/en/stable/installing/>`_ and run:

.. code:: bash

    pip install omf

Or from `github <https://github.com/GMSGDataExchange/omf>`_:

.. code:: bash

    git clone https://github.com/GMSGDataExchange/omf.git
    cd omf
    pip install -e .
