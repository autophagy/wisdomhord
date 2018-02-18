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

  [ COL1          | COL2  | COL3  | COL4        | COL6                       ]
  [ Hello world   | 12345 | True  | Wé          | 28 Regn 226 // 12.11.15    ]
  [ Wes Hál       | 67890 | False | Gárdena     | 10 Mǽdland 226 // 03.43.05 ]
  [ Hallo Welt    | 123   | True  | in          | 8 Mist 226 // 23.23.23     ]
  [ Saluton mondo | 34.2  | False | géardagum   |                            ]
  [ qo' vIvan     | 42    | True  | þéodcyninga | 24 Mǽdland 226 // 01.02.03 ]
  [ Suilad ambar  | 1968  |       | þrym        | 1 Wending 226 // 18.45.55  ]
  [ Ada mūnok     |       | True  | gefrúnon    | 8 Wæstm 226 // 17.10.00    ]


Contents
--------

.. _usage:

.. toctree::
   :maxdepth: 2
   :caption: Usage

   usage/using-a-hord
   usage/bisen
