# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/indexer/indexer_manager/event.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from v4_proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0dydxprotocol/indexer/indexer_manager/event.proto\x12$dydxprotocol.indexer.indexer_manager\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\"~\n\x1dIndexerTendermintEventWrapper\x12K\n\x05\x65vent\x18\x01 \x01(\x0b\x32<.dydxprotocol.indexer.indexer_manager.IndexerTendermintEvent\x12\x10\n\x08txn_hash\x18\x02 \x01(\t\"n\n\x17IndexerEventsStoreValue\x12S\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x43.dydxprotocol.indexer.indexer_manager.IndexerTendermintEventWrapper\"\xe2\x02\n\x16IndexerTendermintEvent\x12\x0f\n\x07subtype\x18\x01 \x01(\t\x12\x1b\n\x11transaction_index\x18\x03 \x01(\rH\x00\x12^\n\x0b\x62lock_event\x18\x04 \x01(\x0e\x32G.dydxprotocol.indexer.indexer_manager.IndexerTendermintEvent.BlockEventH\x00\x12\x13\n\x0b\x65vent_index\x18\x05 \x01(\r\x12\x0f\n\x07version\x18\x06 \x01(\r\x12\x12\n\ndata_bytes\x18\x07 \x01(\x0c\"a\n\nBlockEvent\x12\x1b\n\x17\x42LOCK_EVENT_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x42LOCK_EVENT_BEGIN_BLOCK\x10\x01\x12\x19\n\x15\x42LOCK_EVENT_END_BLOCK\x10\x02\x42\x17\n\x15ordering_within_blockJ\x04\x08\x02\x10\x03\"\xbd\x01\n\x16IndexerTendermintBlock\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\x32\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12L\n\x06\x65vents\x18\x03 \x03(\x0b\x32<.dydxprotocol.indexer.indexer_manager.IndexerTendermintEvent\x12\x11\n\ttx_hashes\x18\x04 \x03(\tBCZAgithub.com/dydxprotocol/v4-chain/protocol/indexer/indexer_managerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.indexer.indexer_manager.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/dydxprotocol/v4-chain/protocol/indexer/indexer_manager'
  _globals['_INDEXERTENDERMINTBLOCK'].fields_by_name['time']._options = None
  _globals['_INDEXERTENDERMINTBLOCK'].fields_by_name['time']._serialized_options = b'\310\336\037\000\220\337\037\001'
  _globals['_INDEXERTENDERMINTEVENTWRAPPER']._serialized_start=145
  _globals['_INDEXERTENDERMINTEVENTWRAPPER']._serialized_end=271
  _globals['_INDEXEREVENTSSTOREVALUE']._serialized_start=273
  _globals['_INDEXEREVENTSSTOREVALUE']._serialized_end=383
  _globals['_INDEXERTENDERMINTEVENT']._serialized_start=386
  _globals['_INDEXERTENDERMINTEVENT']._serialized_end=740
  _globals['_INDEXERTENDERMINTEVENT_BLOCKEVENT']._serialized_start=612
  _globals['_INDEXERTENDERMINTEVENT_BLOCKEVENT']._serialized_end=709
  _globals['_INDEXERTENDERMINTBLOCK']._serialized_start=743
  _globals['_INDEXERTENDERMINTBLOCK']._serialized_end=932
# @@protoc_insertion_point(module_scope)
