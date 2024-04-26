# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from v4_proto.dydxprotocol.blocktime import query_pb2 as dydxprotocol_dot_blocktime_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DowntimeParams = channel.unary_unary(
                '/dydxprotocol.blocktime.Query/DowntimeParams',
                request_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsRequest.SerializeToString,
                response_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsResponse.FromString,
                )
        self.PreviousBlockInfo = channel.unary_unary(
                '/dydxprotocol.blocktime.Query/PreviousBlockInfo',
                request_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoRequest.SerializeToString,
                response_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoResponse.FromString,
                )
        self.AllDowntimeInfo = channel.unary_unary(
                '/dydxprotocol.blocktime.Query/AllDowntimeInfo',
                request_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoRequest.SerializeToString,
                response_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def DowntimeParams(self, request, context):
        """Queries the DowntimeParams.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreviousBlockInfo(self, request, context):
        """Queries the information of the previous block
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllDowntimeInfo(self, request, context):
        """Queries all recorded downtime info.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DowntimeParams': grpc.unary_unary_rpc_method_handler(
                    servicer.DowntimeParams,
                    request_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsRequest.FromString,
                    response_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsResponse.SerializeToString,
            ),
            'PreviousBlockInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.PreviousBlockInfo,
                    request_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoRequest.FromString,
                    response_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoResponse.SerializeToString,
            ),
            'AllDowntimeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.AllDowntimeInfo,
                    request_deserializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoRequest.FromString,
                    response_serializer=dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dydxprotocol.blocktime.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def DowntimeParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.blocktime.Query/DowntimeParams',
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsRequest.SerializeToString,
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryDowntimeParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PreviousBlockInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.blocktime.Query/PreviousBlockInfo',
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoRequest.SerializeToString,
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryPreviousBlockInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllDowntimeInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.blocktime.Query/AllDowntimeInfo',
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoRequest.SerializeToString,
            dydxprotocol_dot_blocktime_dot_query__pb2.QueryAllDowntimeInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
