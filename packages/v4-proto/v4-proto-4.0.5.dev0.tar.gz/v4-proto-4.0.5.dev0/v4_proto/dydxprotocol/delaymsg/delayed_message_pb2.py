# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/delaymsg/delayed_message.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dydxprotocol/delaymsg/delayed_message.proto\x12\x15\x64ydxprotocol.delaymsg\x1a\x19google/protobuf/any.proto\"U\n\x0e\x44\x65layedMessage\x12\n\n\x02id\x18\x01 \x01(\r\x12!\n\x03msg\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0c\x62lock_height\x18\x03 \x01(\rB<Z:github.com/dydxprotocol/v4-chain/protocol/x/delaymsg/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.delaymsg.delayed_message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z:github.com/dydxprotocol/v4-chain/protocol/x/delaymsg/types'
  _globals['_DELAYEDMESSAGE']._serialized_start=97
  _globals['_DELAYEDMESSAGE']._serialized_end=182
# @@protoc_insertion_point(module_scope)
