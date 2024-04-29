NZMATH 3.0.1 (Python 3 calculator on number theory)
===================================================

Introduction
------------

NZMATH is a Python calculator on number theory.  It started development
at Nakamula laboratory, Tokyo Metropolitan University.  Today it is
developed at SourceForge.net .  Download the file NZMATH-3.0.1.tar.gz
for installation from the SourceForge
https://sourceforge.net/projects/nzmath/files/nzmath/ .
Test programs for NZMATH is available as NZMATH-test-3.0.1.tar.gz at
https://sourceforge.net/projects/nzmath/files/nzmath-test/ .

This version 3.0.1 contains several program corrections/additions by
the "notebook" of the book 'Elementary Number Theory' (TAKAGI, Teiji)
in Python-NZMATH language.  On the other hand, the "notebook" itself
is available as an archive NZMATH-enttakagi-0.0.1.tar.gz at
https://sourceforge.net/projects/nzmath/files/nzmath-enttakagi/ .
The "notebook" is designed for beginning students on algorithmic number
theory to self-study Number Theory, Programming and English together.

Installation
------------

To install NZMATH on your computer, you must have Python 3.8 or later.
If you don't have a copy of Python, please install it first.
Python is available from https://www.python.org/ .

The next step is to expand the NZMATH-3.0.1.tar.gz.  The way to do it
depends on your operating system.  On the systems with recent GNU tar,
you can do it with a single command::

 % tar xf NZMATH-3.0.1.tar.gz

Here % is the command line prompt.  Or with standard tar, you can do
it as::

 % gzip -cd NZMATH-3.0.1.tar.gz | tar xf -

Then, you have a child directory named NZMATH-3.0.1 .

The third step is the last step, to install NZMATH to the standard
python path.  Usually, this means to write files to somewhere under
/usr/lib or /usr/local/lib , and thus you have to have appropriate
write permission.  Typically, do as the following::

 % cd NZMATH-3.0.1
 % su
 # python setup.py install

Depending on system, you may get SetuptoolsDeprecationWarning.
Please do not worry for the moment.  Installed NZMATH works well.

Usage
-----

NZMATH is provided as a Python library package named 'nzmath', so
please use it as a usual package.  For more information please refer
Tutorial_.

.. _Tutorial: https://nzmath.sourceforge.io/tutorial.html

Feedback
--------

Your feedbacks are always welcomed.  Please consider to join the
mailing list nzmath-user@lists.sourceforge.net .  You can join the list
by visiting the web page
https://lists.sourceforge.net/lists/listinfo/nzmath-user .

Copyright
---------

NZMATH is distributed under the BSD license.  Please read LICENSE.txt_
in the distribution tar ball for detail.

.. _LICENSE.txt: https://nzmath.sourceforge.io/LICENSE.txt


Copyright (C) 2003-2024, NZMATH development group. All Right Reserved.
(Chief developer: TANAKA, Satoru / Supervisor: NAKAMULA, Ken)
