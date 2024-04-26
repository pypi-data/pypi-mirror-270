# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dydxprotocol/bridge/tx.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v4_proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from v4_proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from v4_proto.dydxprotocol.bridge import bridge_event_pb2 as dydxprotocol_dot_bridge_dot_bridge__event__pb2
from v4_proto.dydxprotocol.bridge import params_pb2 as dydxprotocol_dot_bridge_dot_params__pb2
from v4_proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x64ydxprotocol/bridge/tx.proto\x12\x13\x64ydxprotocol.bridge\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a&dydxprotocol/bridge/bridge_event.proto\x1a dydxprotocol/bridge/params.proto\x1a\x14gogoproto/gogo.proto\"O\n\x15MsgAcknowledgeBridges\x12\x36\n\x06\x65vents\x18\x01 \x03(\x0b\x32 .dydxprotocol.bridge.BridgeEventB\x04\xc8\xde\x1f\x00\"\x1f\n\x1dMsgAcknowledgeBridgesResponse\"\x87\x01\n\x11MsgCompleteBridge\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x35\n\x05\x65vent\x18\x02 \x01(\x0b\x32 .dydxprotocol.bridge.BridgeEventB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1b\n\x19MsgCompleteBridgeResponse\"\x8b\x01\n\x14MsgUpdateEventParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x36\n\x06params\x18\x02 \x01(\x0b\x32 .dydxprotocol.bridge.EventParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1e\n\x1cMsgUpdateEventParamsResponse\"\x8f\x01\n\x16MsgUpdateProposeParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x38\n\x06params\x18\x02 \x01(\x0b\x32\".dydxprotocol.bridge.ProposeParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\" \n\x1eMsgUpdateProposeParamsResponse\"\x8d\x01\n\x15MsgUpdateSafetyParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x37\n\x06params\x18\x02 \x01(\x0b\x32!.dydxprotocol.bridge.SafetyParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x1f\n\x1dMsgUpdateSafetyParamsResponse2\xc7\x04\n\x03Msg\x12t\n\x12\x41\x63knowledgeBridges\x12*.dydxprotocol.bridge.MsgAcknowledgeBridges\x1a\x32.dydxprotocol.bridge.MsgAcknowledgeBridgesResponse\x12h\n\x0e\x43ompleteBridge\x12&.dydxprotocol.bridge.MsgCompleteBridge\x1a..dydxprotocol.bridge.MsgCompleteBridgeResponse\x12q\n\x11UpdateEventParams\x12).dydxprotocol.bridge.MsgUpdateEventParams\x1a\x31.dydxprotocol.bridge.MsgUpdateEventParamsResponse\x12w\n\x13UpdateProposeParams\x12+.dydxprotocol.bridge.MsgUpdateProposeParams\x1a\x33.dydxprotocol.bridge.MsgUpdateProposeParamsResponse\x12t\n\x12UpdateSafetyParams\x12*.dydxprotocol.bridge.MsgUpdateSafetyParams\x1a\x32.dydxprotocol.bridge.MsgUpdateSafetyParamsResponseB:Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dydxprotocol.bridge.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z8github.com/dydxprotocol/v4-chain/protocol/x/bridge/types'
  _globals['_MSGACKNOWLEDGEBRIDGES'].fields_by_name['events']._options = None
  _globals['_MSGACKNOWLEDGEBRIDGES'].fields_by_name['events']._serialized_options = b'\310\336\037\000'
  _globals['_MSGCOMPLETEBRIDGE'].fields_by_name['authority']._options = None
  _globals['_MSGCOMPLETEBRIDGE'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCOMPLETEBRIDGE'].fields_by_name['event']._options = None
  _globals['_MSGCOMPLETEBRIDGE'].fields_by_name['event']._serialized_options = b'\310\336\037\000'
  _globals['_MSGCOMPLETEBRIDGE']._options = None
  _globals['_MSGCOMPLETEBRIDGE']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGUPDATEEVENTPARAMS'].fields_by_name['authority']._options = None
  _globals['_MSGUPDATEEVENTPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEEVENTPARAMS'].fields_by_name['params']._options = None
  _globals['_MSGUPDATEEVENTPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEEVENTPARAMS']._options = None
  _globals['_MSGUPDATEEVENTPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGUPDATEPROPOSEPARAMS'].fields_by_name['authority']._options = None
  _globals['_MSGUPDATEPROPOSEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPROPOSEPARAMS'].fields_by_name['params']._options = None
  _globals['_MSGUPDATEPROPOSEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPROPOSEPARAMS']._options = None
  _globals['_MSGUPDATEPROPOSEPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGUPDATESAFETYPARAMS'].fields_by_name['authority']._options = None
  _globals['_MSGUPDATESAFETYPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATESAFETYPARAMS'].fields_by_name['params']._options = None
  _globals['_MSGUPDATESAFETYPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATESAFETYPARAMS']._options = None
  _globals['_MSGUPDATESAFETYPARAMS']._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGACKNOWLEDGEBRIDGES']._serialized_start=201
  _globals['_MSGACKNOWLEDGEBRIDGES']._serialized_end=280
  _globals['_MSGACKNOWLEDGEBRIDGESRESPONSE']._serialized_start=282
  _globals['_MSGACKNOWLEDGEBRIDGESRESPONSE']._serialized_end=313
  _globals['_MSGCOMPLETEBRIDGE']._serialized_start=316
  _globals['_MSGCOMPLETEBRIDGE']._serialized_end=451
  _globals['_MSGCOMPLETEBRIDGERESPONSE']._serialized_start=453
  _globals['_MSGCOMPLETEBRIDGERESPONSE']._serialized_end=480
  _globals['_MSGUPDATEEVENTPARAMS']._serialized_start=483
  _globals['_MSGUPDATEEVENTPARAMS']._serialized_end=622
  _globals['_MSGUPDATEEVENTPARAMSRESPONSE']._serialized_start=624
  _globals['_MSGUPDATEEVENTPARAMSRESPONSE']._serialized_end=654
  _globals['_MSGUPDATEPROPOSEPARAMS']._serialized_start=657
  _globals['_MSGUPDATEPROPOSEPARAMS']._serialized_end=800
  _globals['_MSGUPDATEPROPOSEPARAMSRESPONSE']._serialized_start=802
  _globals['_MSGUPDATEPROPOSEPARAMSRESPONSE']._serialized_end=834
  _globals['_MSGUPDATESAFETYPARAMS']._serialized_start=837
  _globals['_MSGUPDATESAFETYPARAMS']._serialized_end=978
  _globals['_MSGUPDATESAFETYPARAMSRESPONSE']._serialized_start=980
  _globals['_MSGUPDATESAFETYPARAMSRESPONSE']._serialized_end=1011
  _globals['_MSG']._serialized_start=1014
  _globals['_MSG']._serialized_end=1597
# @@protoc_insertion_point(module_scope)
