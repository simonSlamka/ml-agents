# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents_envs/communicator_objects/capabilities.proto

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
  name='mlagents_envs/communicator_objects/capabilities.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n5mlagents_envs/communicator_objects/capabilities.proto\x12\x14\x63ommunicator_objects\"\xd2\x01\n\x18UnityRLCapabilitiesProto\x12\x1a\n\x12\x62\x61seRLCapabilities\x18\x01 \x01(\x08\x12#\n\x1b\x63oncatenatedPngObservations\x18\x02 \x01(\x08\x12 \n\x18\x63ompressedChannelMapping\x18\x03 \x01(\x08\x12\x15\n\rhybridActions\x18\x04 \x01(\x08\x12\x19\n\x11trainingAnalytics\x18\x05 \x01(\x08\x12!\n\x19variableLengthObservation\x18\x06 \x01(\x08\x42%\xaa\x02\"Unity.MLAgents.CommunicatorObjectsb\x06proto3')
)




_UNITYRLCAPABILITIESPROTO = _descriptor.Descriptor(
  name='UnityRLCapabilitiesProto',
  full_name='communicator_objects.UnityRLCapabilitiesProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='baseRLCapabilities', full_name='communicator_objects.UnityRLCapabilitiesProto.baseRLCapabilities', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concatenatedPngObservations', full_name='communicator_objects.UnityRLCapabilitiesProto.concatenatedPngObservations', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressedChannelMapping', full_name='communicator_objects.UnityRLCapabilitiesProto.compressedChannelMapping', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hybridActions', full_name='communicator_objects.UnityRLCapabilitiesProto.hybridActions', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainingAnalytics', full_name='communicator_objects.UnityRLCapabilitiesProto.trainingAnalytics', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variableLengthObservation', full_name='communicator_objects.UnityRLCapabilitiesProto.variableLengthObservation', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=80,
  serialized_end=290,
)

DESCRIPTOR.message_types_by_name['UnityRLCapabilitiesProto'] = _UNITYRLCAPABILITIESPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityRLCapabilitiesProto = _reflection.GeneratedProtocolMessageType('UnityRLCapabilitiesProto', (_message.Message,), dict(
  DESCRIPTOR = _UNITYRLCAPABILITIESPROTO,
  __module__ = 'mlagents_envs.communicator_objects.capabilities_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityRLCapabilitiesProto)
  ))
_sym_db.RegisterMessage(UnityRLCapabilitiesProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\"Unity.MLAgents.CommunicatorObjects'))
# @@protoc_insertion_point(module_scope)
