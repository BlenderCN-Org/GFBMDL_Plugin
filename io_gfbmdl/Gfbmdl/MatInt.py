# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Gfbmdl

import flatbuffers

class MatInt(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMatInt(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MatInt()
        x.Init(buf, n + offset)
        return x

    # MatInt
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MatInt
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MatInt
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def MatIntStart(builder): builder.StartObject(2)
def MatIntAddName(builder, Name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def MatIntAddValue(builder, Value): builder.PrependInt32Slot(1, Value, 0)
def MatIntEnd(builder): return builder.EndObject()
