# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/indexer/redis/redis_order.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.dydxprotocol.indexer.protocol.v1 import clob_pb2 as dydxprotocol_dot_indexer_dot_protocol_dot_v1_dot_clob__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,dydxprotocol/indexer/redis/redis_order.proto\x12\x1a\x64ydxprotocol.indexer.redis\x1a+dydxprotocol/indexer/protocol/v1/clob.proto\"\xa8\x02\n\nRedisOrder\x12\n\n\x02id\x18\x01 \x01(\t\x12=\n\x05order\x18\x02 \x01(\x0b\x32..dydxprotocol.indexer.protocol.v1.IndexerOrder\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x46\n\x0bticker_type\x18\x04 \x01(\x0e\x32\x31.dydxprotocol.indexer.redis.RedisOrder.TickerType\x12\r\n\x05price\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\t\"Z\n\nTickerType\x12\x1b\n\x17TICKER_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15TICKER_TYPE_PERPETUAL\x10\x01\x12\x14\n\x10TICKER_TYPE_SPOT\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.indexer.redis.redis_order_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REDISORDER']._serialized_start=122
  _globals['_REDISORDER']._serialized_end=418
  _globals['_REDISORDER_TICKERTYPE']._serialized_start=328
  _globals['_REDISORDER_TICKERTYPE']._serialized_end=418
# @@protoc_insertion_point(module_scope)
