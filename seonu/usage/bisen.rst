=====
Bisen
=====

.. _bisen:

To create the data file structure, as well as automate casting to and from
the file, a model called a Bisen should be created and given to Wísdómhord
upon hord creation and loading.

To do this, create a class that inherits from the Bisen class::

    class DocumentationBisen(Bisen):

        __invoker__ = 'Wísdómhord Documentation'
        __description__ = 'Example Bisen for Wísdómhord Documentation'

        col1 = Sweor('COL1', wisdomhord.String)
        col2 = Sweor('COL2', wisdomhord.Boolean)
        col3 = Sweor('COL3', wisdomhord.Integer)
        col4 = Sweor('COL4', wisdomhord.Float)
        col5 = Sweor('COL5', wisdomhord.DateTime)
        col6 = Sweor('COL6', wisdomhord.Wending)

Creating and inserting into a hord using this model would produce a hord that
looks like:

.. code-block:: none

    // INVOKER :: Wísdómhord Insertion Testing
    // DESCRIPTION :: Insertion Test For Wísdómhord
    // INCEPT :: 28 Regn 226
    // UPDATED :: 28 Regn 226
    // COUNT :: 1

    [ COL1   | COL2 | COL3 | COL4 | COL5                   | COL6                   ]
    [ Hello! | True | 10   | 20.3 | 16.02.2018 // 12.11.15 | 28 Regn 226 // 12.11.15]

Reading from this hord while providing this model will return a dictionary for
each row where each cell is cast to the appropriate object - for example ``COL5``
will be returned as a Datetime object.
