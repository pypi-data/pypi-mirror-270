# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/assets/query.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from v4_proto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from v4_proto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from v4_proto.dydxprotocol.assets import asset_pb2 as dydxprotocol_dot_assets_dot_asset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x64ydxprotocol/assets/query.proto\x12\x13\x64ydxprotocol.assets\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1f\x64ydxprotocol/assets/asset.proto\"\x1f\n\x11QueryAssetRequest\x12\n\n\x02id\x18\x01 \x01(\r\"E\n\x12QueryAssetResponse\x12/\n\x05\x61sset\x18\x01 \x01(\x0b\x32\x1a.dydxprotocol.assets.AssetB\x04\xc8\xde\x1f\x00\"S\n\x15QueryAllAssetsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x86\x01\n\x16QueryAllAssetsResponse\x12/\n\x05\x61sset\x18\x01 \x03(\x0b\x32\x1a.dydxprotocol.assets.AssetB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x96\x02\n\x05Query\x12\x81\x01\n\x05\x41sset\x12&.dydxprotocol.assets.QueryAssetRequest\x1a\'.dydxprotocol.assets.QueryAssetResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/dydxprotocol/assets/asset/{id}\x12\x88\x01\n\tAllAssets\x12*.dydxprotocol.assets.QueryAllAssetsRequest\x1a+.dydxprotocol.assets.QueryAllAssetsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/dydxprotocol/assets/assetB:Z8github.com/dydxprotocol/v4-chain/protocol/x/assets/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.assets.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/dydxprotocol/v4-chain/protocol/x/assets/types'
  _globals['_QUERYASSETRESPONSE'].fields_by_name['asset']._options = None
  _globals['_QUERYASSETRESPONSE'].fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _globals['_QUERYALLASSETSRESPONSE'].fields_by_name['asset']._options = None
  _globals['_QUERYALLASSETSRESPONSE'].fields_by_name['asset']._serialized_options = b'\310\336\037\000'
  _globals['_QUERY'].methods_by_name['Asset']._options = None
  _globals['_QUERY'].methods_by_name['Asset']._serialized_options = b'\202\323\344\223\002!\022\037/dydxprotocol/assets/asset/{id}'
  _globals['_QUERY'].methods_by_name['AllAssets']._options = None
  _globals['_QUERY'].methods_by_name['AllAssets']._serialized_options = b'\202\323\344\223\002\034\022\032/dydxprotocol/assets/asset'
  _globals['_QUERYASSETREQUEST']._serialized_start=185
  _globals['_QUERYASSETREQUEST']._serialized_end=216
  _globals['_QUERYASSETRESPONSE']._serialized_start=218
  _globals['_QUERYASSETRESPONSE']._serialized_end=287
  _globals['_QUERYALLASSETSREQUEST']._serialized_start=289
  _globals['_QUERYALLASSETSREQUEST']._serialized_end=372
  _globals['_QUERYALLASSETSRESPONSE']._serialized_start=375
  _globals['_QUERYALLASSETSRESPONSE']._serialized_end=509
  _globals['_QUERY']._serialized_start=512
  _globals['_QUERY']._serialized_end=790
# @@protoc_insertion_point(module_scope)
