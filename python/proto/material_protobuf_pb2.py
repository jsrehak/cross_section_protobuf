# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: material_protobuf.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='material_protobuf.proto',
  package='material_protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\x17material_protobuf.proto\x12\x11material_protobuf\"\xe9\x06\n\x07Library\x12\x14\n\x0clibrary_name\x18\x01 \x01(\t\x12\x18\n\x10number_of_groups\x18\x02 \x01(\r\x12\x19\n\renergy_groups\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x36\n\tmaterials\x18\x04 \x03(\x0b\x32#.material_protobuf.Library.Material\x1a\xca\x04\n\x08Material\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x62\x62reviation\x18\x02 \x01(\t\x12\t\n\x01\x41\x18\x03 \x01(\r\x12\t\n\x01Z\x18\x04 \x01(\r\x12K\n\x0fscalar_property\x18\x05 \x03(\x0b\x32\x32.material_protobuf.Library.Material.ScalarProperty\x12K\n\x0fvector_property\x18\x06 \x03(\x0b\x32\x32.material_protobuf.Library.Material.VectorProperty\x12K\n\x0fmatrix_property\x18\x07 \x03(\x0b\x32\x32.material_protobuf.Library.Material.MatrixProperty\x1aP\n\x0eScalarProperty\x12/\n\x02id\x18\x01 \x01(\x0e\x32#.material_protobuf.Library.ScalarId\x12\r\n\x05value\x18\x02 \x01(\x02\x1aT\n\x0eVectorProperty\x12/\n\x02id\x18\x01 \x01(\x0e\x32#.material_protobuf.Library.VectorId\x12\x11\n\x05value\x18\x02 \x03(\x01\x42\x02\x10\x01\x1ap\n\x0eMatrixProperty\x12/\n\x02id\x18\x01 \x01(\x0e\x32#.material_protobuf.Library.MatrixId\x12\x0c\n\x04rows\x18\x02 \x01(\r\x12\x0c\n\x04\x63ols\x18\x03 \x01(\r\x12\x11\n\x05value\x18\x04 \x03(\x01\x42\x02\x10\x01\"+\n\x08ScalarId\x12\x12\n\x0eUNKNOWN_SCALAR\x10\x00\x12\x0b\n\x07\x44\x45NSITY\x10\x01\"4\n\x08VectorId\x12\x12\n\x0eUNKNOWN_VECTOR\x10\x00\x12\x0b\n\x07SIGMA_T\x10\x01\x12\x07\n\x03\x43HI\x10\x02\"+\n\x08MatrixId\x12\x12\n\x0eUNKNOWN_MATRIX\x10\x00\x12\x0b\n\x07SIGMA_S\x10\x01\x62\x06proto3')
)



_LIBRARY_SCALARID = _descriptor.EnumDescriptor(
  name='ScalarId',
  full_name='material_protobuf.Library.ScalarId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SCALAR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DENSITY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=778,
  serialized_end=821,
)
_sym_db.RegisterEnumDescriptor(_LIBRARY_SCALARID)

_LIBRARY_VECTORID = _descriptor.EnumDescriptor(
  name='VectorId',
  full_name='material_protobuf.Library.VectorId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VECTOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMA_T', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHI', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=823,
  serialized_end=875,
)
_sym_db.RegisterEnumDescriptor(_LIBRARY_VECTORID)

_LIBRARY_MATRIXID = _descriptor.EnumDescriptor(
  name='MatrixId',
  full_name='material_protobuf.Library.MatrixId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MATRIX', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMA_S', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=877,
  serialized_end=920,
)
_sym_db.RegisterEnumDescriptor(_LIBRARY_MATRIXID)


_LIBRARY_MATERIAL_SCALARPROPERTY = _descriptor.Descriptor(
  name='ScalarProperty',
  full_name='material_protobuf.Library.Material.ScalarProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='material_protobuf.Library.Material.ScalarProperty.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='material_protobuf.Library.Material.ScalarProperty.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=576,
)

_LIBRARY_MATERIAL_VECTORPROPERTY = _descriptor.Descriptor(
  name='VectorProperty',
  full_name='material_protobuf.Library.Material.VectorProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='material_protobuf.Library.Material.VectorProperty.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='material_protobuf.Library.Material.VectorProperty.value', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=578,
  serialized_end=662,
)

_LIBRARY_MATERIAL_MATRIXPROPERTY = _descriptor.Descriptor(
  name='MatrixProperty',
  full_name='material_protobuf.Library.Material.MatrixProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='material_protobuf.Library.Material.MatrixProperty.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='material_protobuf.Library.Material.MatrixProperty.rows', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cols', full_name='material_protobuf.Library.Material.MatrixProperty.cols', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='material_protobuf.Library.Material.MatrixProperty.value', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=664,
  serialized_end=776,
)

_LIBRARY_MATERIAL = _descriptor.Descriptor(
  name='Material',
  full_name='material_protobuf.Library.Material',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_name', full_name='material_protobuf.Library.Material.full_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abbreviation', full_name='material_protobuf.Library.Material.abbreviation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A', full_name='material_protobuf.Library.Material.A', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Z', full_name='material_protobuf.Library.Material.Z', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scalar_property', full_name='material_protobuf.Library.Material.scalar_property', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_property', full_name='material_protobuf.Library.Material.vector_property', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matrix_property', full_name='material_protobuf.Library.Material.matrix_property', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LIBRARY_MATERIAL_SCALARPROPERTY, _LIBRARY_MATERIAL_VECTORPROPERTY, _LIBRARY_MATERIAL_MATRIXPROPERTY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=776,
)

_LIBRARY = _descriptor.Descriptor(
  name='Library',
  full_name='material_protobuf.Library',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='library_name', full_name='material_protobuf.Library.library_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_groups', full_name='material_protobuf.Library.number_of_groups', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy_groups', full_name='material_protobuf.Library.energy_groups', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='materials', full_name='material_protobuf.Library.materials', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LIBRARY_MATERIAL, ],
  enum_types=[
    _LIBRARY_SCALARID,
    _LIBRARY_VECTORID,
    _LIBRARY_MATRIXID,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=920,
)

_LIBRARY_MATERIAL_SCALARPROPERTY.fields_by_name['id'].enum_type = _LIBRARY_SCALARID
_LIBRARY_MATERIAL_SCALARPROPERTY.containing_type = _LIBRARY_MATERIAL
_LIBRARY_MATERIAL_VECTORPROPERTY.fields_by_name['id'].enum_type = _LIBRARY_VECTORID
_LIBRARY_MATERIAL_VECTORPROPERTY.containing_type = _LIBRARY_MATERIAL
_LIBRARY_MATERIAL_MATRIXPROPERTY.fields_by_name['id'].enum_type = _LIBRARY_MATRIXID
_LIBRARY_MATERIAL_MATRIXPROPERTY.containing_type = _LIBRARY_MATERIAL
_LIBRARY_MATERIAL.fields_by_name['scalar_property'].message_type = _LIBRARY_MATERIAL_SCALARPROPERTY
_LIBRARY_MATERIAL.fields_by_name['vector_property'].message_type = _LIBRARY_MATERIAL_VECTORPROPERTY
_LIBRARY_MATERIAL.fields_by_name['matrix_property'].message_type = _LIBRARY_MATERIAL_MATRIXPROPERTY
_LIBRARY_MATERIAL.containing_type = _LIBRARY
_LIBRARY.fields_by_name['materials'].message_type = _LIBRARY_MATERIAL
_LIBRARY_SCALARID.containing_type = _LIBRARY
_LIBRARY_VECTORID.containing_type = _LIBRARY
_LIBRARY_MATRIXID.containing_type = _LIBRARY
DESCRIPTOR.message_types_by_name['Library'] = _LIBRARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), dict(

  Material = _reflection.GeneratedProtocolMessageType('Material', (_message.Message,), dict(

    ScalarProperty = _reflection.GeneratedProtocolMessageType('ScalarProperty', (_message.Message,), dict(
      DESCRIPTOR = _LIBRARY_MATERIAL_SCALARPROPERTY,
      __module__ = 'material_protobuf_pb2'
      # @@protoc_insertion_point(class_scope:material_protobuf.Library.Material.ScalarProperty)
      ))
    ,

    VectorProperty = _reflection.GeneratedProtocolMessageType('VectorProperty', (_message.Message,), dict(
      DESCRIPTOR = _LIBRARY_MATERIAL_VECTORPROPERTY,
      __module__ = 'material_protobuf_pb2'
      # @@protoc_insertion_point(class_scope:material_protobuf.Library.Material.VectorProperty)
      ))
    ,

    MatrixProperty = _reflection.GeneratedProtocolMessageType('MatrixProperty', (_message.Message,), dict(
      DESCRIPTOR = _LIBRARY_MATERIAL_MATRIXPROPERTY,
      __module__ = 'material_protobuf_pb2'
      # @@protoc_insertion_point(class_scope:material_protobuf.Library.Material.MatrixProperty)
      ))
    ,
    DESCRIPTOR = _LIBRARY_MATERIAL,
    __module__ = 'material_protobuf_pb2'
    # @@protoc_insertion_point(class_scope:material_protobuf.Library.Material)
    ))
  ,
  DESCRIPTOR = _LIBRARY,
  __module__ = 'material_protobuf_pb2'
  # @@protoc_insertion_point(class_scope:material_protobuf.Library)
  ))
_sym_db.RegisterMessage(Library)
_sym_db.RegisterMessage(Library.Material)
_sym_db.RegisterMessage(Library.Material.ScalarProperty)
_sym_db.RegisterMessage(Library.Material.VectorProperty)
_sym_db.RegisterMessage(Library.Material.MatrixProperty)


_LIBRARY_MATERIAL_VECTORPROPERTY.fields_by_name['value'].has_options = True
_LIBRARY_MATERIAL_VECTORPROPERTY.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_LIBRARY_MATERIAL_MATRIXPROPERTY.fields_by_name['value'].has_options = True
_LIBRARY_MATERIAL_MATRIXPROPERTY.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_LIBRARY.fields_by_name['energy_groups'].has_options = True
_LIBRARY.fields_by_name['energy_groups']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
