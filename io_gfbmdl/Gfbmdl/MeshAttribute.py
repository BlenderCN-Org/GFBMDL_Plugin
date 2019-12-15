# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Gfbmdl

import flatbuffers

class MeshAttribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMeshAttribute(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MeshAttribute()
        x.Init(buf, n + offset)
        return x

    # MeshAttribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MeshAttribute
    def VertexType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MeshAttribute
    def BufferFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MeshAttribute
    def ElementCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def MeshAttributeStart(builder): builder.StartObject(3)
def MeshAttributeAddVertexType(builder, VertexType): builder.PrependUint32Slot(0, VertexType, 0)
def MeshAttributeAddBufferFormat(builder, BufferFormat): builder.PrependUint32Slot(1, BufferFormat, 0)
def MeshAttributeAddElementCount(builder, ElementCount): builder.PrependUint32Slot(2, ElementCount, 0)
def MeshAttributeEnd(builder): return builder.EndObject()
