# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from v4_proto.dydxprotocol.feetiers import query_pb2 as dydxprotocol_dot_feetiers_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PerpetualFeeParams = channel.unary_unary(
                '/dydxprotocol.feetiers.Query/PerpetualFeeParams',
                request_serializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsRequest.SerializeToString,
                response_deserializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsResponse.FromString,
                )
        self.UserFeeTier = channel.unary_unary(
                '/dydxprotocol.feetiers.Query/UserFeeTier',
                request_serializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierRequest.SerializeToString,
                response_deserializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def PerpetualFeeParams(self, request, context):
        """Queries the PerpetualFeeParams.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserFeeTier(self, request, context):
        """Queries a user's fee tier
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PerpetualFeeParams': grpc.unary_unary_rpc_method_handler(
                    servicer.PerpetualFeeParams,
                    request_deserializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsRequest.FromString,
                    response_serializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsResponse.SerializeToString,
            ),
            'UserFeeTier': grpc.unary_unary_rpc_method_handler(
                    servicer.UserFeeTier,
                    request_deserializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierRequest.FromString,
                    response_serializer=dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dydxprotocol.feetiers.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def PerpetualFeeParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.feetiers.Query/PerpetualFeeParams',
            dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsRequest.SerializeToString,
            dydxprotocol_dot_feetiers_dot_query__pb2.QueryPerpetualFeeParamsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserFeeTier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dydxprotocol.feetiers.Query/UserFeeTier',
            dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierRequest.SerializeToString,
            dydxprotocol_dot_feetiers_dot_query__pb2.QueryUserFeeTierResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
