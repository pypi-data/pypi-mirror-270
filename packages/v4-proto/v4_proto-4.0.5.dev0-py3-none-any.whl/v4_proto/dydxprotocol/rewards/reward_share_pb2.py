# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/rewards/reward_share.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from v4_proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dydxprotocol/rewards/reward_share.proto\x12\x14\x64ydxprotocol.rewards\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"\x92\x01\n\x0bRewardShare\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12X\n\x06weight\x18\x02 \x01(\x0c\x42H\xc8\xde\x1f\x00\xda\xde\x1f@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableIntB;Z9github.com/dydxprotocol/v4-chain/protocol/x/rewards/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.rewards.reward_share_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z9github.com/dydxprotocol/v4-chain/protocol/x/rewards/types'
  _globals['_REWARDSHARE'].fields_by_name['address']._options = None
  _globals['_REWARDSHARE'].fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_REWARDSHARE'].fields_by_name['weight']._options = None
  _globals['_REWARDSHARE'].fields_by_name['weight']._serialized_options = b'\310\336\037\000\332\336\037@github.com/dydxprotocol/v4-chain/protocol/dtypes.SerializableInt'
  _globals['_REWARDSHARE']._serialized_start=115
  _globals['_REWARDSHARE']._serialized_end=261
# @@protoc_insertion_point(module_scope)
