# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/clob/liquidations.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from v4_proto.dydxprotocol.subaccounts import subaccount_pb2 as dydxprotocol_dot_subaccounts_dot_subaccount__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$dydxprotocol/clob/liquidations.proto\x12\x11\x64ydxprotocol.clob\x1a\x14gogoproto/gogo.proto\x1a)dydxprotocol/subaccounts/subaccount.proto\"u\n\x18PerpetualLiquidationInfo\x12\x43\n\rsubaccount_id\x18\x01 \x01(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cperpetual_id\x18\x02 \x01(\r\"x\n\x19SubaccountLiquidationInfo\x12\x1d\n\x15perpetuals_liquidated\x18\x01 \x03(\r\x12\x1b\n\x13notional_liquidated\x18\x02 \x01(\x04\x12\x1f\n\x17quantums_insurance_lost\x18\x03 \x01(\x04\"\xdf\x01\n\x1aSubaccountOpenPositionInfo\x12\x14\n\x0cperpetual_id\x18\x01 \x01(\r\x12T\n\x1esubaccounts_with_long_position\x18\x02 \x03(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x12U\n\x1fsubaccounts_with_short_position\x18\x03 \x03(\x0b\x32&.dydxprotocol.subaccounts.SubaccountIdB\x04\xc8\xde\x1f\x00\x42\x38Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.clob.liquidations_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/dydxprotocol/v4-chain/protocol/x/clob/types'
  _globals['_PERPETUALLIQUIDATIONINFO'].fields_by_name['subaccount_id']._options = None
  _globals['_PERPETUALLIQUIDATIONINFO'].fields_by_name['subaccount_id']._serialized_options = b'\310\336\037\000'
  _globals['_SUBACCOUNTOPENPOSITIONINFO'].fields_by_name['subaccounts_with_long_position']._options = None
  _globals['_SUBACCOUNTOPENPOSITIONINFO'].fields_by_name['subaccounts_with_long_position']._serialized_options = b'\310\336\037\000'
  _globals['_SUBACCOUNTOPENPOSITIONINFO'].fields_by_name['subaccounts_with_short_position']._options = None
  _globals['_SUBACCOUNTOPENPOSITIONINFO'].fields_by_name['subaccounts_with_short_position']._serialized_options = b'\310\336\037\000'
  _globals['_PERPETUALLIQUIDATIONINFO']._serialized_start=124
  _globals['_PERPETUALLIQUIDATIONINFO']._serialized_end=241
  _globals['_SUBACCOUNTLIQUIDATIONINFO']._serialized_start=243
  _globals['_SUBACCOUNTLIQUIDATIONINFO']._serialized_end=363
  _globals['_SUBACCOUNTOPENPOSITIONINFO']._serialized_start=366
  _globals['_SUBACCOUNTOPENPOSITIONINFO']._serialized_end=589
# @@protoc_insertion_point(module_scope)
