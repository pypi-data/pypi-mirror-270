# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/indexer/socks/messages.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.dydxprotocol.indexer.protocol.v1 import subaccount_pb2 as dydxprotocol_dot_indexer_dot_protocol_dot_v1_dot_subaccount__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dydxprotocol/indexer/socks/messages.proto\x12\x1a\x64ydxprotocol.indexer.socks\x1a\x31\x64ydxprotocol/indexer/protocol/v1/subaccount.proto\"K\n\x10OrderbookMessage\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x14\n\x0c\x63lob_pair_id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\"\xca\x01\n\x11SubaccountMessage\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\t\x12\x19\n\x11transaction_index\x18\x02 \x01(\x05\x12\x13\n\x0b\x65vent_index\x18\x03 \x01(\r\x12\x10\n\x08\x63ontents\x18\x04 \x01(\t\x12L\n\rsubaccount_id\x18\x05 \x01(\x0b\x32\x35.dydxprotocol.indexer.protocol.v1.IndexerSubaccountId\x12\x0f\n\x07version\x18\x06 \x01(\t\"]\n\x0cTradeMessage\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\t\x12\x10\n\x08\x63ontents\x18\x04 \x01(\t\x12\x14\n\x0c\x63lob_pair_id\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x06 \x01(\t\"2\n\rMarketMessage\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x97\x02\n\rCandleMessage\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x14\n\x0c\x63lob_pair_id\x18\x02 \x01(\t\x12H\n\nresolution\x18\x03 \x01(\x0e\x32\x34.dydxprotocol.indexer.socks.CandleMessage.Resolution\x12\x0f\n\x07version\x18\x04 \x01(\t\"\x82\x01\n\nResolution\x12\x0e\n\nONE_MINUTE\x10\x00\x12\x10\n\x0c\x46IVE_MINUTES\x10\x01\x12\x13\n\x0f\x46IFTEEN_MINUTES\x10\x02\x12\x12\n\x0eTHIRTY_MINUTES\x10\x03\x12\x0c\n\x08ONE_HOUR\x10\x04\x12\x0e\n\nFOUR_HOURS\x10\x05\x12\x0b\n\x07ONE_DAY\x10\x06\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.indexer.socks.messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORDERBOOKMESSAGE']._serialized_start=124
  _globals['_ORDERBOOKMESSAGE']._serialized_end=199
  _globals['_SUBACCOUNTMESSAGE']._serialized_start=202
  _globals['_SUBACCOUNTMESSAGE']._serialized_end=404
  _globals['_TRADEMESSAGE']._serialized_start=406
  _globals['_TRADEMESSAGE']._serialized_end=499
  _globals['_MARKETMESSAGE']._serialized_start=501
  _globals['_MARKETMESSAGE']._serialized_end=551
  _globals['_CANDLEMESSAGE']._serialized_start=554
  _globals['_CANDLEMESSAGE']._serialized_end=833
  _globals['_CANDLEMESSAGE_RESOLUTION']._serialized_start=703
  _globals['_CANDLEMESSAGE_RESOLUTION']._serialized_end=833
# @@protoc_insertion_point(module_scope)
