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


from PyQt5 import QtCore, Qt3DExtras, Qt3DCore
from PyQt5.QtGui import QQuaternion, QVector3D, QColor


class SceneModifier(QtCore.QObject):
    def __init__(self, rootEntity):
        super(SceneModifier, self).__init__(rootEntity)
        # Torus shape data
        self.m_torus = Qt3DExtras.QTorusMesh()
        self.m_torus.setRadius(1.0)
        self.m_torus.setMinorRadius(0.4)
        self.m_torus.setRings(100)
        self.m_torus.setSlices(20)

        # TorusMesh Transform
        torusTransform = Qt3DCore.QTransform()
        torusTransform.setScale(2.0)
        torusTransform.setRotation(QQuaternion.fromAxisAndAngle(QVector3D(0.0, 1.0, 0.0), 25.0))
        torusTransform.setTranslation(QVector3D(5.0, 4.0, 0.0))

        torusMaterial = Qt3DExtras.QPhongMaterial()
        torusMaterial.setDiffuse(QColor('#beb32b'))

        # Torus
        self.m_torusEntity = Qt3DCore.QEntity(rootEntity)
        self.m_torusEntity.addComponent(self.m_torus)
        self.m_torusEntity.addComponent(torusMaterial)
        self.m_torusEntity.addComponent(torusTransform)

        # Cone shape data
        cone = Qt3DExtras.QConeMesh()
        cone.setTopRadius(0.5)
        cone.setBottomRadius(1)
        cone.setLength(3)
        cone.setRings(50)
        cone.setSlices(20)

        # ConeMesh Transform
        coneTransform = Qt3DCore.QTransform()
        coneTransform.setScale(1.5)
        coneTransform.setRotation(QQuaternion.fromAxisAndAngle(QVector3D(1.0, 0.0, 0.0), 45.0))
        coneTransform.setTranslation(QVector3D(0.0, 4.0, -1.5))

        coneMaterial = Qt3DExtras.QPhongMaterial()
        coneMaterial.setDiffuse(QColor('#928327'))

        # Cone
        self.m_coneEntity = Qt3DCore.QEntity(rootEntity)
        self.m_coneEntity.addComponent(cone)
        self.m_coneEntity.addComponent(coneMaterial)
        self.m_coneEntity.addComponent(coneTransform)

        # Cylinder shape data
        cylinder = Qt3DExtras.QCylinderMesh()
        cylinder.setRadius(1)
        cylinder.setLength(3)
        cylinder.setRings(100)
        cylinder.setSlices(20)

        # CylinderMesh Transform
        cylinderTransform = Qt3DCore.QTransform()
        cylinderTransform.setScale(1.5)
        cylinderTransform.setRotation(QQuaternion.fromAxisAndAngle(QVector3D(1.0, 0.0, 0.0), 45.0))
        cylinderTransform.setTranslation(QVector3D(-5.0, 4.0, -1.5))

        cylinderMaterial = Qt3DExtras.QPhongMaterial()
        cylinderMaterial.setDiffuse(QColor('#928327'))

        # Cylinder
        self.m_cylinderEntity = Qt3DCore.QEntity(rootEntity)
        self.m_cylinderEntity.addComponent(cylinder)
        self.m_cylinderEntity.addComponent(cylinderMaterial)
        self.m_cylinderEntity.addComponent(cylinderTransform)

        # Cuboid shape data
        cuboid = Qt3DExtras.QCuboidMesh()

        # CuboidMesh Transform
        cuboidTransform = Qt3DCore.QTransform()
        cuboidTransform.setScale(4.0)
        cuboidTransform.setTranslation(QVector3D(5.0, -4.0, 0.0))

        cuboidMaterial = Qt3DExtras.QPhongMaterial()
        cuboidMaterial.setDiffuse(QColor('#665423'))

        # Cuboid
        self.m_cuboidEntity = Qt3DCore.QEntity(rootEntity)
        self.m_cuboidEntity.addComponent(cuboid)
        self.m_cuboidEntity.addComponent(cuboidMaterial)
        self.m_cuboidEntity.addComponent(cuboidTransform)

        # Plane shape data
        planeMesh = Qt3DExtras.QPlaneMesh()
        planeMesh.setWidth(2)
        planeMesh.setHeight(2)

        # Plane mesh transform
        planeTransform = Qt3DCore.QTransform()
        planeTransform.setScale(1.3)
        planeTransform.setRotation(QQuaternion.fromAxisAndAngle(QVector3D(1.0, 0.0, 0.0), 45.0))
        planeTransform.setTranslation(QVector3D(0.0, -4.0, 0.0))

        planeMaterial = Qt3DExtras.QPhongMaterial()
        planeMaterial.setDiffuse(QColor('#a69929'))

        # Plane
        self.m_planeEntity = Qt3DCore.QEntity(rootEntity)
        self.m_planeEntity.addComponent(planeMesh)
        self.m_planeEntity.addComponent(planeMaterial)
        self.m_planeEntity.addComponent(planeTransform)

        # Sphere shape data
        sphereMesh = Qt3DExtras.QSphereMesh()
        sphereMesh.setRings(20)
        sphereMesh.setSlices(20)
        sphereMesh.setRadius(2)

        # Sphere mesh transform
        sphereTransform = Qt3DCore.QTransform()

        sphereTransform.setScale(1.3)
        sphereTransform.setTranslation(QVector3D(-5.0, -4.0, 0.0))

        sphereMaterial = Qt3DExtras.QPhongMaterial()
        sphereMaterial.setDiffuse(QColor('#a69929'))

        # Sphere
        m_sphereEntity = Qt3DCore.QEntity(rootEntity)
        m_sphereEntity.addComponent(sphereMesh)
        m_sphereEntity.addComponent(sphereMaterial)
        m_sphereEntity.addComponent(sphereTransform)

    def enableTorus(self, enabled):
        self.m_torusEntity.setEnabled(enabled)

    def enableCone(self, enabled):
        self.m_coneEntity.setEnabled(enabled)

    def enableCylinder(self, enabled):
        self.m_cylinderEntity.setEnabled(enabled)

    def enableCuboid(self, enabled):
        self.m_cuboidEntity.setEnabled(enabled)

    def enablePlane(self, enabled):
        self.m_planeEntity.setEnabled(enabled)

    def enableSphere(self, enabled):
        self.m_sphereEntity.setEnabled(enabled)
