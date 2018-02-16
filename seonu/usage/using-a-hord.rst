============
Using a Hord
============

Wísdómhord currently only supports row insertion and reading. Future versions
will support updating existing rows as well as row deletion.

Creation
========

To create a new hord, supply the desired path and the :doc:`bisen` you wish to use::

    hord = wisdomhord.cennan('/home/user/doc.hord', bisen=YourBisen)

This will return a Wisdomhord object ready for you to use. If the file already
exists, the cennan will fail.

Loading
=======

To load an existing hord, supply the path to the hord as well as the bisen::

    hord = wisdomhord.hladan('/home/user/doc.hord', bisen=YourBisen)

Insertion
=========

To insert into a hord that you have created or loaded, first define the column
value dictionary you want to insert::

    row = {'COL1': 'Hello!',
           'COL2': True,
           'COL3': 10,
           'COL4': 20.3,
           'COL5': datetime.datetime(2018, 2, 16, 12, 11, 15)}

    hord.insert(row)

Reading
=======

To retrieve the rows from a hord, you can::

    rows = hord.get_rows()

This will return all the rows in the hord, ordered by their order in the file.

You can also limit by the number of rows returned::

    rows = hord.get_rows(limit=10)

or by the desired columns::

    rows = hord.get_rows(cols=['COL2', 'COL3'])

The returned rows can also be sorted by a column::

    rows = hord.get_rows(sort_by=['COL3'], reverse_sort=True)

The returned rows can also be filtred by a supplied function::

    rows = hord.get_rows(filter_func=lambda x: x['COL2'] == True and x['COL3'] >= 10)
