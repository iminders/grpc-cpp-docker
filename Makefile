proto:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./calculator_service.proto

serv:
	docker run --rm -it -p 8080:8080 aiminders/cpp-grpc-demo:latest

client:
	python3 client.py
