#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_sequence.widget.interfaces module

This module defines internal references widgets interfaces.
"""

from zope.interface import Attribute
from pyams_skin.interfaces.widget import IDynamicSelectWidget


__docformat__ = 'restructuredtext'


class IInternalReferenceWidget(IDynamicSelectWidget):
    """Internal reference widget"""

    ajax_url = Attribute("AJAX search endpoint URL")


class IInternalReferencesListWidget(IDynamicSelectWidget):
    """Internal references list widget"""

    ajax_url = Attribute("AJAX search endpoint URL")
