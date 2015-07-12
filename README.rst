ugetch
======
utf-8 getch, with support for arrows, tab, echoing, etc

.. image:: https://travis-ci.org/toejough/ugetch.svg
   :target: https://travis-ci.org/toejough/ugetch
   
.. image:: https://codeclimate.com/github/toejough/ugetch/badges/gpa.svg
   :target: https://codeclimate.com/github/toejough/ugetch
   :alt: Code Climate
   
.. image:: https://badge.waffle.io/toejough/ugetch.svg?label=ready&title=Ready 
 :target: https://waffle.io/toejough/ugetch 
 :alt: 'Stories in Ready'

* `api`_
* `contribution`_

API
===

* `getkey`_

getkey
------

Gets a "key" from the ``infile`` and returns it to the user, where "key" is a character or glyph.
Currently supports parsing ASCII and UTF-8.
Any other keys entered (such as arrow keys, UTF-16, etc) will result in returning individual bytes, one at a time.

Parameters:

* ``infile`` - defaults to the ``sys.stdin`` file, as it is set at call time.

Returns:

* ``key`` - a string value corresponding to the key read in from the TTY ('a', 'B', '-', etc).

contribution
============

Contributions welcome!  See the issues for current things that need to be addressed.

When you contribute, please:

* Run the tests before you change things, to make sure that you have a good version downloaded.  They should all pass.
* Add sufficient tests to exercise the new behavior you're adding.
* Run those before you push.
* Add sufficient documentation to explain your changed behavior.
* Use the below template in your final commit.

Pull requests with insufficient tests, failing tests, poor quality (as rated by code-climate_, currently) or insufficient documentation will be sent back to the author or back-burnered.

.. _code-climate: https://codeclimate.com/github/toejough/ugetch

contribution template
---------------------

I use SPATD.  Spatted?  Spatd?  I don't know, it doesn't make a great pronouncable acronym, but it's a great way to cover all the angles for a given change.
::

  Summary: <a one-line summary, which includes text to close the issue the commit addresses.>
  
  **Problem:**
  <Describe the problem you are solving.  This should generally be a summary of the issue.>
  
  **Analysis:**
  <Analysis of the problem, such as root-cause-analysis of the problem.>
  <Analysis of the solution, such as what is the chosen solution and why.>
  <Any other analysis/thoughts about this issue/solution.>
  
  **Testing:**
  <What testing was performed.  Preferably automated tests.>
  <If none, an explanation of why none was performed/added.>
  
  **Documentation:**
  <What documentation was added.>
  <If none, an explanation of why none was added.>
