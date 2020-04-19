run:
	./lancache.py cache-domains/ "10.0.0.141" > Corefile
restart:
	docker restart coredns
stop:
	docker stop coredns
start:
	docker start coredns
new:
	docker run --name=coredns -v ${PWD}:/root/ --expose=53 -p 53:53/udp --restart=always --detach=true coredns/coredns -conf /root/Corefile
rm:
	docker stop coredns && docker rm coredns
logs:
	docker logs -f coredns
default: run
