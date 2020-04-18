# pihole-ddns
Auto-populate pihole DNS with local DNS from your router

## Idea
My modem/router's DHCP DNS system is pretty flakey. After a reboot it loses all its smarts even though the leases don't expire. I'm annoyed when I type in a local hostname and it doesn't resolve. I'm also looking for a nice solution for caching downloads (like steam games and apt packages)

I'm looking to leverage PiHole as my DNS, but not my DHCP system (DHCP works fine and I want it to work in a downed Pi world)

So here are my thoughts for a topology:

+ Modem serves DHCP requests
  + This is less work for me
  + If the pi goes down, we still have DHCP
  + Modem handles static/dynamic addresses just fine
+ Don't disable DNS on the modem
  + DO change what DNS hosts DHCP gives out
  + DNS 1 should be the PiHole (10.0.0.x)
  + DNS 2 should be itself (10.0.0.1) in case the PiHole is down (something is better than nothing)
  + Modem still does DHCP <-> DNS hostname mapping (THIS IS IMPORTANT)
+ PiHole DNS for its software stack, not adblocking (unless you want it)
  + I'm going with PiHole because I think it's the nicest DNS server I can deal with right now
  + Bind was getting too complicated for this, plus GUIs aren't as easy to find packaged
  + I'll probably not use the PiHole's adblocking feature, but that's just personal perferance
  + Leveraging this trick: https://discourse.pi-hole.net/t/howto-using-pi-hole-as-lan-dns-server/533 is going to be the idea of this repo (building a config based on nmap data)
  + We'll make use of what I've already built here: https://github.com/jrcichra/mappi
+ (Optional) Lancache
  + Use what I've learned with the lancache project (and my arm fork) to foward DNS requests to certain domains "upstream" to a different raspberry pi with storage attached
  + See this repo for my pi version: https://github.com/jrcichra/lancache-rpi
  + I have a feeling forwarding a series of domains will be challenging
  + Will likely need to write some parser like how lancache does with their listings: https://github.com/uklans/cache-domains
  + PiHole will need to forward those to lancache