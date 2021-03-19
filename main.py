#****************************************************************************
#
# Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
# Contact: https://www.qt.io/licensing/
#
# This file is part of the Qt3D module of the Qt Toolkit.
#
# $QT_BEGIN_LICENSE:BSD$
# Commercial License Usage
# Licensees holding valid commercial Qt licenses may use this file in
# accordance with the commercial license agreement provided with the
# Software or, alternatively, in accordance with the terms contained in
# a written agreement between you and The Qt Company. For licensing terms
# and conditions see https://www.qt.io/terms-conditions. For further
# information use the contact form at https://www.qt.io/contact-us.
#
# BSD License Usage
# Alternatively, you may use this file under the terms of the BSD license
# as follows:
#
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of The Qt Company Ltd nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
#
# $QT_END_LICENSE$
#
#****************************************************************************
from PyQt5.QtGui import QColor, QVector3D
from PyQt5.QtCore import QSize, Qt
from PyQt5 import Qt3DCore, Qt3DRender, Qt3DExtras, QtWidgets

from scenemodifier import SceneModifier

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    view = Qt3DExtras.Qt3DWindow()
    view.defaultFrameGraph().setClearColor(QColor('#4d4d4f'))
    container = QtWidgets.QWidget.createWindowContainer(view)
    screenSize = view.screen().size()
    container.setMinimumSize(QSize(200, 100))
    container.setMaximumSize(screenSize)

    widget = QtWidgets.QWidget()
    hLayout = QtWidgets.QHBoxLayout(widget)
    vLayout = QtWidgets.QVBoxLayout()
    vLayout.setAlignment(Qt.AlignTop)
    hLayout.addWidget(container, 1)
    hLayout.addLayout(vLayout)
    widget.setWindowTitle('Basic shapes')

    # Root entity
    rootEntity = Qt3DCore.QEntity()

    # Camera
    cameraEntity = view.camera()

    cameraEntity.lens().setPerspectiveProjection(45.0, 16.0/9.0, 0.1, 1000.0)
    cameraEntity.setPosition(QVector3D(0, 0, 20.0))
    cameraEntity.setUpVector(QVector3D(0, 1, 0))
    cameraEntity.setViewCenter(QVector3D(0, 0, 0))

    lightEntity = Qt3DCore.QEntity(rootEntity)
    light = Qt3DRender.QPointLight(lightEntity)
    light.setColor(QColor("white"))
    light.setIntensity(1)
    lightEntity.addComponent(light)
    lightTransform = Qt3DCore.QTransform(lightEntity)
    lightTransform.setTranslation(cameraEntity.position())
    lightEntity.addComponent(lightTransform)

    # For camera controls
    camController = Qt3DExtras.QFirstPersonCameraController(rootEntity)
    camController.setCamera(cameraEntity)

    # Scenemodifier
    modifier = SceneModifier(rootEntity)

    # Set root object of the scene
    view.setRootEntity(rootEntity)

    # Create control widgets
    info = QtWidgets.QCommandLinkButton();
    info.setText('Qt3D ready-made meshes');
    info.setDescription('Qt3D provides several ready-made meshes, like torus, cylinder, cone, '
                        'cube, plane and sphere.')
    info.setIconSize(QSize(0,0))

    torusCB = QtWidgets.QCheckBox(widget)
    torusCB.setChecked(True)
    torusCB.setText('Torus')

    coneCB = QtWidgets.QCheckBox(widget)
    coneCB.setChecked(True)
    coneCB.setText('Cone')

    cylinderCB = QtWidgets.QCheckBox(widget)
    cylinderCB.setChecked(True)
    cylinderCB.setText('Cylinder')

    cuboidCB = QtWidgets.QCheckBox(widget)
    cuboidCB.setChecked(True)
    cuboidCB.setText('Cuboid')

    planeCB = QtWidgets.QCheckBox(widget)
    planeCB.setChecked(True)
    planeCB.setText('Plane')

    sphereCB = QtWidgets.QCheckBox(widget)
    sphereCB.setChecked(True)
    sphereCB.setText('Sphere')

    vLayout.addWidget(info)
    vLayout.addWidget(torusCB)
    vLayout.addWidget(coneCB)
    vLayout.addWidget(cylinderCB)
    vLayout.addWidget(cuboidCB)
    vLayout.addWidget(planeCB)
    vLayout.addWidget(sphereCB)

    torusCB.stateChanged.connect(modifier.enableTorus)
    coneCB.stateChanged.connect(modifier.enableCone)
    cylinderCB.stateChanged.connect(modifier.enableCylinder)
    cuboidCB.stateChanged.connect(modifier.enableCuboid)
    planeCB.stateChanged.connect(modifier.enablePlane)
    sphereCB.stateChanged.connect(modifier.enableSphere)

    torusCB.setChecked(True)
    coneCB.setChecked(True)
    cylinderCB.setChecked(True)
    cuboidCB.setChecked(True)
    planeCB.setChecked(True)
    sphereCB.setChecked(True)

    # Show window
    widget.show();
    widget.resize(1200, 800)

    app.exec_()
