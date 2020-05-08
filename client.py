from __future__ import print_function

import logging

import grpc

import calculator_service_pb2
import calculator_service_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('127.0.0.1:8080') as channel:
        stub = calculator_service_pb2_grpc.CalculatorStub(channel)
        response = stub.Compute(
            calculator_service_pb2.ComputeRequest(lhs=1.1, rhs=2.2))
    print("caculator client received: %.3f" % response.result)


if __name__ == '__main__':
    logging.basicConfig()
    run()
