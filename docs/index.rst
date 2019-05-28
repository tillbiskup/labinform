LabInform documentation
=======================

Welcome! This is the documentation for LabInform, in particular its components written in Python. For general information see its `homepage <https://www.labinform.de/>`_.

LabInform is a framework and toolchain for **reproducible research**, focussing on free and open-source software components. Integral parts are an **electronic lab notebook** (ELN) based on `DokuWiki <https://www.dokuwiki.org/>`_, a **datasafe** as central storage for all your valuable data, and **unique identifiers** (*Lab Object Identifier*, LOI, much like the well-known DOIs) for datasets, samples, and alike.

Together with `LabInform <https://www.LabInform.de/>`_ (*Analysis of Spectral Data*), a framework for handling spectroscopic data focussing on reproducibility, it forms the basis of fully reproducible research without additional costs.


Features
--------

A list of features, not all implemented yet but aimed at for the first public release (LabInform 0.1):

* Datasafe -- a home to your precious data (both, experimental and calculated)

* Lab Object Identifier (LOI) -- unique identifiers for samples, data, ...

* Electronic Lab Notebook (ELN) -- automated access from processing routines


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.5)

* Extensive user and API documentation



.. warning::
  LabInform is currently under active development and still considered in Alpha development state. Therefore, expect frequent changes in features and public APIs that may break your own code. Nevertheless, feedback as well as feature requests are highly welcome.



Where to start
--------------

Users new to LabInform should probably start :doc:`at the beginning <audience>`, those familiar with its :doc:`underlying concepts <concepts>` an planning to help in further developing may jump straight to the section explaining how to :doc:`contribute to the development of LabInform <developers>`.

The :doc:`API documentation <api/index>` is the definite source of information for developers, besides having a look at the source code.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   audience
   introduction
   concepts
   components
   subpackages
   developers
   api/index



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



A note on the logo
------------------

The "L" originates from the Computer Modern Roman font originally designed by Donald E. Knuth for his TeX typesetting system. As such, it represents science and the scientific method. Harbouring the "i" representing the information bit puts things right: Proper and reproducible science is the solid support for all the information we can retrieve. The copyright of the logo belongs to J. Popp.
