========
Overview
========

Wísdómhord is a flat file db format and tool for internal project use.

The goal is to create a flat file db format that produces something that makes
sense to check into git - both in the sense that it produces meanginful diffs,
and that it is immediately readable.

An example hord looks like:

.. code-block:: none

  // INVOKER :: Wísdómhord
  // DESCRIPTION :: An example hord
  // INCEPT :: 10 Regn 226 // 05.00
  // UPDATED :: 10 Regn 226 // 05.40
  // COUNT :: 7

  [ COL1          | COL2  | COL3  | COL4        ]
  [ Hello world   | 12345 | True  | Wé          ]
  [ Wes Hál       | 67890 | False | Gárdena     ]
  [ Hallo Welt    | 123   | True  | in          ]
  [ Saluton mondo | 34.2  | False | géardagum   ]
  [ qo' vIvan     | 42    | True  | þéodcyninga ]
  [ Suilad ambar  | 1968  |       | þrym        ]
  [ Ada mūnok     |       | True  | gefrúnon    ]


Contents
--------

.. _usage:

.. toctree::
   :maxdepth: 2
   :caption: Usage

   usage/using-a-hord
   usage/bisen
