# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Gfbmdl

import flatbuffers

class Mesh(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMesh(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Mesh()
        x.Init(buf, n + offset)
        return x

    # Mesh
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Mesh
    def Polygons(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .MeshPolygon import MeshPolygon
            obj = MeshPolygon()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Mesh
    def PolygonsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Mesh
    def Attributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .MeshAttribute import MeshAttribute
            obj = MeshAttribute()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Mesh
    def AttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Mesh
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Mesh
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Mesh
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def MeshStart(builder): builder.StartObject(3)
def MeshAddPolygons(builder, Polygons): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Polygons), 0)
def MeshStartPolygonsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MeshAddAttributes(builder, Attributes): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Attributes), 0)
def MeshStartAttributesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def MeshAddData(builder, Data): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Data), 0)
def MeshStartDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MeshEnd(builder): return builder.EndObject()
