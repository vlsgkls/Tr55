# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Tr55
                                 A QGIS plugin
 Transform QGIS data into WinTR-55 input data.
                             -------------------
        begin                : 2015-06-12
        copyright            : (C) 2015 by Gkorgkolis Vasileios
        email                : vgkorgko@topo.auth.gr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Tr55 class from file Tr55.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .tr_55 import Tr55
    return Tr55(iface)
