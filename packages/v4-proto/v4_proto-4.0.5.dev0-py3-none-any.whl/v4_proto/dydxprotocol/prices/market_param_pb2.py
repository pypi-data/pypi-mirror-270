# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/prices/market_param.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&dydxprotocol/prices/market_param.proto\x12\x13\x64ydxprotocol.prices\"\x8c\x01\n\x0bMarketParam\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04pair\x18\x02 \x01(\t\x12\x10\n\x08\x65xponent\x18\x03 \x01(\x11\x12\x15\n\rmin_exchanges\x18\x04 \x01(\r\x12\x1c\n\x14min_price_change_ppm\x18\x05 \x01(\r\x12\x1c\n\x14\x65xchange_config_json\x18\x06 \x01(\tB:Z8github.com/dydxprotocol/v4-chain/protocol/x/prices/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.prices.market_param_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/dydxprotocol/v4-chain/protocol/x/prices/types'
  _globals['_MARKETPARAM']._serialized_start=64
  _globals['_MARKETPARAM']._serialized_end=204
# @@protoc_insertion_point(module_scope)
