# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/nft/v1beta1/nft.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmos/nft/v1beta1/nft.proto\x12\x12\x63osmos.nft.v1beta1\x1a\x19google/protobuf/any.proto\"\x89\x01\n\x05\x43lass\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t\x12\x10\n\x08uri_hash\x18\x06 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32\x14.google.protobuf.Any\"f\n\x03NFT\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x10\n\x08uri_hash\x18\x04 \x01(\t\x12\"\n\x04\x64\x61ta\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyB\x14Z\x12\x63osmossdk.io/x/nftb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.nft.v1beta1.nft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\022cosmossdk.io/x/nft'
  _globals['_CLASS']._serialized_start=80
  _globals['_CLASS']._serialized_end=217
  _globals['_NFT']._serialized_start=219
  _globals['_NFT']._serialized_end=321
# @@protoc_insertion_point(module_scope)
