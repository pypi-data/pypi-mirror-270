# -*- coding: UTF-8 -*-
"""
:filename: sppas.ui.whakerpy.httpd.__init__.py
:author:   Brigitte Bigi
:contact:  contact@sppas.org
:summary:  Manage an HTTPD server and a handler for any web-based app.

.. _This file is part of SPPAS: https://sppas.org/
..
    -------------------------------------------------------------------------

     ___   __    __    __    ___
    /     |  \  |  \  |  \  /              the automatic
    \__   |__/  |__/  |___| \__             annotation and
       \  |     |     |   |    \             analysis
    ___/  |     |     |   | ___/              of speech

    Copyright (C) 2011-2023  Brigitte Bigi
    Laboratoire Parole et Langage, Aix-en-Provence, France

    Use of this software is governed by the GNU Public License, version 3.

    SPPAS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    SPPAS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with SPPAS. If not, see <https://www.gnu.org/licenses/>.

    This banner notice must not be removed.

    -------------------------------------------------------------------------

"""

from .hstatus import HTTPDValueError
from .hstatus import HTTPDStatus
from .hutils import HTTPDHandlerUtils
from .handler import HTTPDHandler
from .hserver import BaseHTTPDServer
from .hresponse import BaseResponseRecipe

__all__ = (
    "BaseResponseRecipe",
    "HTTPDStatus",
    "HTTPDValueError",
    "HTTPDHandler",
    "HTTPDHandlerUtils",
    "BaseHTTPDServer"
)
