# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from v4_proto.dydxprotocol.blocktime import tx_pb2 as dydxprotocol_dot_blocktime_dot_tx__pb2


class MsgStub(object):
    """Msg defines the Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateDowntimeParams = channel.unary_unary(
                '/dydxprotocol.blocktime.Msg/UpdateDowntimeParams',
                request_serializer=dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParams.SerializeToString,
                response_deserializer=dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParamsResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the Msg service.
    """

    def UpdateDowntimeParams(self, request, context):
        """UpdateDowntimeParams updates the DowntimeParams in state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateDowntimeParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDowntimeParams,
                    request_deserializer=dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParams.FromString,
                    response_serializer=dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dydxprotocol.blocktime.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the Msg service.
    """

    @staticmethod
    def UpdateDowntimeParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.blocktime.Msg/UpdateDowntimeParams',
            dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParams.SerializeToString,
            dydxprotocol_dot_blocktime_dot_tx__pb2.MsgUpdateDowntimeParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
