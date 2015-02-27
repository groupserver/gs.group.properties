=======================
``gs.group.properties``
=======================
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Change the group properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-02-19
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product provides the basic `Change properties`_ form, and
the `Properties viewlet manager`_.

Change Properties
=================

The *Change properties* form, ``changeproperties.html`` in the
Group context, provides a page for changing the basic group
properties (such as the name).

Properties Viewlet Manager
==========================

The *Properties* viewlet manager provides a list of links to the
*site* administrator, to allow him or her to change the group
properties:

.. code-block:: xml

  <browser:viewlet 
    name="gs-group-messages-ratelimit-home-admin-tab"
    manager="gs.group.properties.interfaces.IGroupAdminPropertiesLinks"
    template="browser/templates/adminlist.pt"
    class="gs.group.member.viewlet.GroupAdminViewlet"
    permission="zope2.ManageUsers"
    weight="5"
    title="Change the posting rate" />

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.properties
- Translations:
  https://www.transifex.com/projects/p/gs-group-properties/
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

..  LocalWords:  changeproperties html
