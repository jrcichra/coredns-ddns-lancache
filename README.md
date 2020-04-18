# coredns-ddns-lancache
My config/scripts for a coreDNS, Dynamic DNS, and lancache solution

## Idea
My modem/router's DHCP DNS system is pretty flakey. After a reboot it loses all its smarts even though the leases don't expire. I'm annoyed when I type in a local hostname and it doesn't resolve. I'm also looking for a nice solution for caching downloads (like steam games and apt packages)

I'm looking to leverage CoreDNS as my DNS, but not my DHCP system (DHCP works fine and I want it to work in a downed Pi world)

So here are my thoughts for a topology:

+ Modem serves DHCP requests
  + This is less work for me
  + If the pi goes down, we still have DHCP
  + Modem handles static/dynamic addresses just fine
+ Don't disable DNS on the modem
  + DO change what DNS hosts DHCP gives out
  + DNS 1 should be the Pi (10.0.0.x)
  + DNS 2 should be itself (10.0.0.1) in case CoreDNS is down (something is better than nothing)
  + Modem still does DHCP <-> DNS hostname mapping (THIS IS IMPORTANT)
+ CoreDNS for its flexability
  + Bind was getting too complicated and felt old
  + I do stuff with kubernetes so this will be transferrable knowledge
  + Keep a local hosts file populated with what I get from nmap
  + We'll make use of what I've already built here: https://github.com/jrcichra/mappi (database of the most recently known hostnames <-> IPs from nmap)
+ (Optional) Lancache
  + Use what I've learned with the lancache project (and my arm fork) to foward DNS requests to certain domains "upstream" to a different raspberry pi with storage attached
  + See this repo for my pi version: https://github.com/jrcichra/lancache-rpi
  + I have a feeling forwarding a series of domains will be challenging
  + Will likely need to write some little parser to forward lancache listings: https://github.com/uklans/cache-domains
  + CoreDNS will need to forward those to lancache