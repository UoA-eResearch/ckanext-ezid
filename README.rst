.. image:: https://travis-ci.org/UoA-eResearch/ckanext-ezid.svg?branch=master
  :target: https://travis-ci.org/UoA-eResearch/ckanext-ezid


.. image:: https://coveralls.io/repos/UoA-eResearch/ckanext-ezid/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/UoA-eResearch/ckanext-ezid?branch=master


=============
ckanext-ezid
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!

This extension provides an interface to `EZID
<http://ezid.cdlib.org/>`_ for `ckanext-external_id
<https://github.com/UoA-eResearch/ckanext-external_id>`_.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-ezid:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-ezid Python package into your virtual environment::

     cd src
     git clone https://github.com/UoA-eResearch/ckanext-ezid.git
     cd ckanext-ezid
     python setup.py develop
     
3. Add ``ezid`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Set your EZID username, password and namespace with the keys
    ckan.ezid.username,
    ckan.ezid.password,
    ckan.ezid.namespace
   in your CKAN config file

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

