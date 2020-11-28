# Part 2 - Networking

### Notes

###### Introduction to Networking

Protocols are a defined set of standards that computers must follow in order to communicate properly. Computer networking is the name we’ve given to the full scope of how computers communicate with each other.

#### The TCP/IP Five-layer Network Model

Physical Layer. Represents physical devices that connect computers. Data Link Layer. Responsible for defining a common way of interpreting these signals so network devices can communicate. Network Layer. Allows different networks to communicate with each other through devices known as routers. The most common protocol followed here is IP. It delivers data between two individual nodes. Transport Layer. Sorts out which client and server programs are supposed to get that data. TCP is the protocol most commonly used in this layer. Application Layer. Application-specific protocols are followed. The primary difference between this five-layer model and the OSI model is that the OSI model abstracts the application layer into three layers total.

Networking Devices. Cables connect different devices to each other, allowing data to be transmitted over them may be of copper which transmits data using electric pulses. Crosstalk is when an electrical pulse on one wire is accidentally detected on another wire. Fiber cables contain individual optical fibers which are tiny tubes made out of glass and transmit data using light. Hub is a physical layer device that allows connections from many computers at once. The collision domain is a network segment where only one device can communicate at a time. A switching hub is a better alternative. They are primary devices used to connect computers on a single network, referred to as LAN. A router is a device that knows how to forward data between independent networks.

##### The Physical Layer

Its main focus is on transmitting bits (1’s and 0’s ) from one end of the link to the next. In copper wires, it is transmitted using modulation which is varying voltage of this charge moving across the cable. Duplex communication is the concept that information can flow in both directions across the cable.

##### The Data Link Layer

The protocol most widely used to send data across individual links is Ethernet. The primary purpose is to abstract away for any other layer to care about the physical layers and hardware. CSMA/CD is used to determine when a communication channel is clear and when a device is free to transmit data. MAC address is a globally unique identifier attached to an individual network interface. MAC address is represented by 4 octets (hexadecimal numbers). Ethernet uses MAC addresses to ensure that the data it sends has both addresses for transmitter and receiver. Unicast transmission is for one receiving address. A broadcast is for all devices in a local network. This is accomplished using a special destination known as the broadcast address. Data Packet is an all-encompassing term that represents any single set of binary data being sent across a network link and is known as ethernet frames at the ethernet level. Ethernet frame is a highly structured collection of information presented in a specific order. This used to convert those traveling bits into meaningful data. Ethernet frame has a particular format that contains the header, mac addresses, data payload (original data).

##### The Network Layer

IP addresses are made up of four octets. IP Addresses belong to networks, not to the devices attached to those networks. The IP address assigned automatically to a newly connected device using DHCP (Dynamic Host Configuration Protocol). A data packet here in this layer is referred to as an IP datagram (A highly structured series of fields that are strictly defined). IP datagram’s header contains several fields such as total length, source and destination IP Address, identification etc. The entire content of an IP datagram is encapsulated as the payload of an ethernet frame. IP Address splits into two sections: Network ID, Host ID. Divided into class A,B,C,D according to partition between both sections. ADR (Address resolution protocol) is a protocol to discover the hardware address of a node with a certain IP Address. ARP Table is a list of IP Addresses and the mac addresses associated with them.

Subnetting is the process of taking a large network and splitting it up into many individual and smaller subnetworks, or subnets. Network IDs are used to identify networks whereas Host IDs to identify hosts. Subnet ID is a part of Host ID and is calculated using subnet masks. A subnet mask is a 32-bit number with all 1’s in beginning followed by 0’s at the end. Eg. 255.255.255.0. The purpose of all ones is to tell what part of an IP address is the subnet ID. The purpose of all zeros is to tell what part of an IP is available for hosts. CIDR (Classless Inter-Domain Routing)is more flexible approach to define blocks of an IP. Demarcation Point is to describe when one netowrk ends and other begins.

Router is a network device that forwards traffic depending on the destination address of that traffic. After receiving data packet a router examines its destination IP and looks up for IP destination network in routing table and then forwards traffic to destination. Most basic routing table example contains four columns: destination network, Next hop (next router that should receive data), Total hop (shortest possible path), Interface (which of the interface it has to forward traffic). Routing protocols are used for communication between routers divided in 2 categories: Interior gateway protocols, exterior gateway protocols. Interior gateway protocols are used by routers to share information within a single autonomous system. autonomous system is collection of networks under a single network operator. Interior protocols have 2 types: link-state protocol, distance vector protocol. Exterior gateway protocol are used to communicate between routers representing the edges of an autonomous system. ASN are numbers assigned to individual autonomous systems. Non-routable address spaces are ranges of IPs set aside for use by anyone that cannot be routed to.  

##### The Transport Layer

Transport layer is responsibe for functions like multiplexing, demultiplexing, estabilishing long connections and ensuring data integrity through error checking and data verification. Port is a 16 bit number that's used to direct traffic to specific services running on a networked computer. Port 80 for http, port 21 for ftp. port combined with IP is known as socket address. An IP datagram encapsulates TCP segment. TCP segment have various fields like source and destination ports, control flags, payload. There are 6 types of control flags: 1. URG(Urgent) 2. ACK(Acknowledged) 3. PSH(Push) 4. RST(Reset) 5. FIN(Finish). A TCP connection is established using a three way handshake. SYN, SYN/ACK, ACK flags. Connection ends with a four way handshake: FIN, ACK, FIN, ACK. A socket is the instantiation of an end-point in a potential TCP connection. LISTEN (listening for incoming connections), SYN_SENT (synchronization request sent), SYN_RECEIVED (after receiving syn request sends a syn/ack back), ESTABLISHED (tcp connection working) are some of the socket states. A firewall is a device that blocks traffic that meets certain criteria.

##### The Application Layer

Protocol to be used to communicate depends on the type of application.

#### Networking services

DNS (Domain Name System) is a global and highly distributed network service that resolves strings of letters into IP Addresses for you. DNS also helps organization resolves their domain to different IPs. There are 5 types of DNS servers. Caching and recursive name server's purpose is to store known domain name lookups for a certain amount of time. TTL(time to live) is a value in seconds that can be congfigured by the owner of a domain name for how long a server is allowed to cache an entry before it should discard it and perform a full resolution. In a full resolution, recursive servers contacts to root servers, root server respond to DNS lookup with TLD(top level domain like .com) that should be queried, Corresponding TLD server will respond to DNS lookup by pointing it to authoritive name server. So the name server will finally provide the IP to the recursive(client) server. 

Resource record types. An A record is used to point a certain domain name at a certain IPv4 address. Ouad A points to IPv6. A CNAME record is used to redirect traffic from one domain to another. MX record is used to deliver e-mail to the correct server.

Every computer must have four things specifically configured: an IP, subnet mask, primary gateway, DNS server. DHCP (Dynamic host Configuration Protocol) is an application layer protocol that automates the configuration process of hosts on a network. Dynamic allocation is done in which a range of IP addresses is set aside for client devices and one of these IPs is issued to these devices when they request one. Fixed allocation is a process which requires a manually specified list of MAC Addresses and their corresponding IPs. The process by which a client configured to use DHCP attempts to get network configuration information is known as DHCP discovery.

Network Address Translation (NAT) translates one IP address into another. It allows a gateway usually a router or firewall, to rewrite the source IP of an outgoing datagram while retaining the original IP in order to rewrite it into the response. IP masquerading is a security concept of hiding IPs of computers communicating with other.

VPN (Virtual Private Networks) is a technology that allows for the extension of a private or a local network to hosts that might not be on that local network. It uses encrypted tunnels to connect to networks to which they are not physically connected to.

A proxy service is a server that acts on behalf of a client in order to access another service. A reverse proxy is a service that might appear to be a single server to external clients, but actually represents many servers living behind it.

##### Connecting to the Internet

A dial-up connection uses POTS (old telephone service) to transmit data and gets its name because the connection is established by actually dialing a phone number and is done through modems (for digital and analog conversions)

Broadband Connections are any connectivity technology that isn't dial-up internet. T-carrier technology allowed lots of phone calls to travel across a single cable simultaneously using twisted copper wire cables.

Wide Area Network (WAN) acts like a single network, but spans across multiple physical locations.   
