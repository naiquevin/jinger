Jinger - Jinga2 based static site generator
===========================================

What is Jinger ?
----------------

Jinger is a static site (not blog) generator that brings the power and
convenience of Jinja2_ python template engine for developing static html
sites. Template inheritance was the main motivation behind developing it,
therefore the use of jinja2 and hence the name ``Jinger``!

Why another static site generator ?
-----------------------------------

Ok, to be frank, (as always) I didn't check other alternatives before
starting to write code. Also I liked the name that I came up with!

Anyway, I was looking for something that solved the problem of
writing and maintaining multiple static web pages using the same
layout that allowed code reuse and better organization at the same
time. Most of the other stuff I found was more focussed on blogging.

Features
--------

- Command for generating site directory structure with configurable names
  for directories.
- Development Server.

Dependencies
------------

Nothing other than Jinja2.::

    $ pip install Jinja2


Install
-------

Run following command to install (Virtualenv recommended)::

    $ cd jinger
    $ python setup.py install


Uninstall
---------

Jinger can be uninstalled using pip

    $ pip uninstall jinger


Usage
-----

Start a new site::

    $ jinger startsite <sitename> [options]

      [options] 
      -s or --sourcedir name of the source template dir [default: templates]
      -t or --targetdir name of the target dir [default: public]

Generate html from templates::

    $ cd mysite
    $ jinger generate

Run development server::

    $ cd mysite
    $ jinger runserver [options]
    
    [options]
    -p or --port

Help::

    $ jinger help


Editing templates
-----------------

TODO

Html directory tree will be same as the templates directory tree

Important: Templates starting with ``base`` are expected to be base
templates which other templates will extend and hence will not be
generated to html.

See ``examples/mysite`` for more info and next section for running the
examples.


Webassets
---------

When jinger creates a new site upon running the ``startsite`` command,
a directory named ``webassets`` is also created where you should place
any css, js, images etc for your site. Note that the choice of name
for this directory is not configurable unlike the ``sourcedir`` and
``targetdir`` directories.  This is because the generate command will
copy all the contents of this dir into the ``targetdir`` from where it
will be served.

for eg. if you have following files and directories inside webassets ::

    webassets/
             js/
               main.js
             css/
                styles.css
             images/
                   logo.png

After running ``generate`` these will be copied to ``targetdir`` as ::

    public/
          js/
            main.js
          css/
             styles.css
          images/
                logo.png


Note however that when running the development server, these files
will be served directly from inside ``webassets``.

Including the webassets in your jinja2 template files
-----------------------------------------------------

To include the css/js/images in the templates, just use their path
relative to ``webassets`` such as ::

    <link rel="stylesheet" type="text/css" href="css/styles.css"/>


Running the example
-------------------

Examples can be run without installation as follows:

To create a new site, first create a symlink of ``jinger/commands.py``
inside ``examples`` or any other directory where you want to use the
commands (These symlinks will be ignored by git)::

    $ cd examples
    $ ln -s ../jinger/commands.py commands.py
    $ python commands.py startsite newsite
    $ cd newsite
    $ ln -s ../../jinger/commands.py commands.py
    $ echo "<h1>It works!</h1>" > templates/index.html
    $ python commands.py runserver

Then open http://127.0.0.1:9000/ in your favourite browser.

To compile templates to markup::
    
    $ cd newsite
    $ python commands.py generate


Running Tests
-------------

Use the test runner module to run tests as follows::

    $ cd jinger
    $ python testrunner.py # will run all tests in jinger/test
    $ python testrunner.py site # will run jinger/test/test_site.py

When the tests are run, directories and files will be created in ``playground``
directory and will be deleted in tearDown. Ignore this dir if you don't need 
to run tests.


Roadmap
-------

Please see ``roadmap.org``.


Bugs
----

Please use github issue tracker to submit any bugs

All kinds of feedback is welcome :)

.. _Jinga2: http://jinja.pocoo.org/

