# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\"I\n\x0fLocationMessage\x12\x11\n\tperson_id\x18\x01 \x01(\t\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t2?\n\x0fLocationService\x12,\n\x06\x43reate\x12\x10.LocationMessage\x1a\x10.LocationMessageb\x06proto3')



_LOCATIONMESSAGE = DESCRIPTOR.message_types_by_name['LocationMessage']
LocationMessage = _reflection.GeneratedProtocolMessageType('LocationMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONMESSAGE,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationMessage)
  })
_sym_db.RegisterMessage(LocationMessage)

_LOCATIONSERVICE = DESCRIPTOR.services_by_name['LocationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCATIONMESSAGE._serialized_start=18
  _LOCATIONMESSAGE._serialized_end=91
  _LOCATIONSERVICE._serialized_start=93
  _LOCATIONSERVICE._serialized_end=156
# @@protoc_insertion_point(module_scope)
