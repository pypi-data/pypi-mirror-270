# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from v4_proto.dydxprotocol.bridge import tx_pb2 as dydxprotocol_dot_bridge_dot_tx__pb2


class MsgStub(object):
    """Msg defines the Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AcknowledgeBridges = channel.unary_unary(
                '/dydxprotocol.bridge.Msg/AcknowledgeBridges',
                request_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridges.SerializeToString,
                response_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridgesResponse.FromString,
                )
        self.CompleteBridge = channel.unary_unary(
                '/dydxprotocol.bridge.Msg/CompleteBridge',
                request_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridge.SerializeToString,
                response_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridgeResponse.FromString,
                )
        self.UpdateEventParams = channel.unary_unary(
                '/dydxprotocol.bridge.Msg/UpdateEventParams',
                request_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParams.SerializeToString,
                response_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParamsResponse.FromString,
                )
        self.UpdateProposeParams = channel.unary_unary(
                '/dydxprotocol.bridge.Msg/UpdateProposeParams',
                request_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParams.SerializeToString,
                response_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParamsResponse.FromString,
                )
        self.UpdateSafetyParams = channel.unary_unary(
                '/dydxprotocol.bridge.Msg/UpdateSafetyParams',
                request_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParams.SerializeToString,
                response_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParamsResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the Msg service.
    """

    def AcknowledgeBridges(self, request, context):
        """AcknowledgeBridges acknowledges bridges and sets them to complete at a
        later block.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteBridge(self, request, context):
        """CompleteBridge finalizes a bridge by minting coins to an address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEventParams(self, request, context):
        """UpdateEventParams updates the EventParams in state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProposeParams(self, request, context):
        """UpdateProposeParams updates the ProposeParams in state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSafetyParams(self, request, context):
        """UpdateSafetyParams updates the SafetyParams in state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AcknowledgeBridges': grpc.unary_unary_rpc_method_handler(
                    servicer.AcknowledgeBridges,
                    request_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridges.FromString,
                    response_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridgesResponse.SerializeToString,
            ),
            'CompleteBridge': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteBridge,
                    request_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridge.FromString,
                    response_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridgeResponse.SerializeToString,
            ),
            'UpdateEventParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEventParams,
                    request_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParams.FromString,
                    response_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParamsResponse.SerializeToString,
            ),
            'UpdateProposeParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProposeParams,
                    request_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParams.FromString,
                    response_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParamsResponse.SerializeToString,
            ),
            'UpdateSafetyParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateSafetyParams,
                    request_deserializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParams.FromString,
                    response_serializer=dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dydxprotocol.bridge.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the Msg service.
    """

    @staticmethod
    def AcknowledgeBridges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.bridge.Msg/AcknowledgeBridges',
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridges.SerializeToString,
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgAcknowledgeBridgesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteBridge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.bridge.Msg/CompleteBridge',
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridge.SerializeToString,
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgCompleteBridgeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEventParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.bridge.Msg/UpdateEventParams',
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParams.SerializeToString,
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateEventParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProposeParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.bridge.Msg/UpdateProposeParams',
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParams.SerializeToString,
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateProposeParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateSafetyParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.bridge.Msg/UpdateSafetyParams',
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParams.SerializeToString,
            dydxprotocol_dot_bridge_dot_tx__pb2.MsgUpdateSafetyParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
