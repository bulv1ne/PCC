PCC (or Python Clean Code)
==========================

PCC streamlines execution of `isort` and `black`. This tool is like a bash `alias` or executing 2 commands in your terminal.
This didn't stop me to create a new Python package (though not deployed on PyPI), this serves for me personally
to train and write documentation.

How to use PCC:

.. code-block::

    python -m pcc
    # or
    pcc

Test your code:

.. code-block::

    python -m pcc --test
    # or
    pcc --test


Features
--------

- Execute isort and black for you.


Installation
------------

Install PCC by cloning this repo and installing it:

.. code-block::

    git clone git@github.com:bulv1ne/PCC.git
    pip install --user PCC

Or installing through git+https immediately:

.. code-block::

    pip install git+https://github.com/bulv1ne/PCC.git


Contribute
----------

- Issue Tracker: https://github.com/bulv1ne/PCC/issues
- Source Code: https://github.com/bulv1ne/PCC


Support
-------

If you are having issues, please let us know by creating an issue on Github.


License
-------

The project is licensed under the MIT license.
