# Part 1-Technical Support Fundamentals

### Notes

##### Introduction to IT support

The use of technology like computers and the internet to store and process data into some useful information. IT helps people solve meaningful problems by using technology. A computer is a device that stores and processes data by performing calculations. An algorithm is a series of steps that solve specific problems.  open-source software can be freely distributed, modified, and shared. Cryptography is an art of writing and solving codes.

##### Digital Logic

Binary system, the communication that a computer uses- base 2 numeral system. 8 bits = 1 byte. 1 byte can store 1 character. Character encoding: assigns our binary values to characters. UTF-8: lets us a variable number of bytes. 3 bytes for RGB to represent the color of a pixel. Logic Gates: Allows our transistor to do more complex tasks depending on logical conditions.

##### Computer Architecture Layer

A computer can be cut into four main layers: Hardware, Operating systems, Software, Users. Hardware is physical components, operating systems allows hardware to communicate with the systems, the software layer is how we humans interact with our computer

##### Hardware

Ports are connection points that we connect devices to extend the functionality of our computer. CPU(central processing unit) is the brain of our computer. RAM( random access memory) is our computer’s short-term memory. The hard drive holds all our data permanently. The motherboard holds everything and lets everything communicate. Programs are instructions we give to computers to what to do. External Data Bus (EDB) is a row of wires that transports binary data. MCC (memory controller chip) is intermediate for CPU and ram. Caches are a fast way to access memory as it only stores recently or frequently used data divided into three levels L1, L2, L3. The internal clock is there in the clock connected through a clock wire. Clock speed is the maximum number of cycles that CPU can handle in a certain time period (eg. 3.4Ghz).

CPU. Hard-coded with instruction sets. Two major types of CPU sockets: Land Grid Array(LGA),  Pin Grid Array(PGA). Heat sink to prevent overheating. 32 bit and 64-bit architecture of CPU are its capacity to handle data efficiently. RAM. To store data that needs to be accessed quickly. DRAM (dynamic) is commonly found. DDR4 is the fastest RAM available till now. MotherBoard. Chipset decides how components talk to each other on our machine. It also has expansion slots to enhance the functionality of the computer. The Form Factor is the amount of space we can have. Storage Solid-state drives(SSD) works similar to USB lot faster than HDDs and are less prone to damage. Power Supplies. To convert ac voltage to dc voltage. Mobile devices use SoC(System on a Chip) that packs the CPU, ram, storage onto a single chip. A charge cycle is one full charge and discharge of the battery. Peripherals are external devices we connect like mice. Type C connectors are used nowadays to transfer audio, video, power, data. BIOS. Basic input-output services, a software that initializes hardware in our computer and gets OS up and running. BIOS is stored in ROM (read-only memory chip), ROM is non-volatile.

##### Operating Systems

OS is the whole package that manages computer resources and lets us interact with them. Divided into two main parts: KERNEL Space (Process manager, memory manager, File manager, I/O management) | User Space (Applications, User Interfaces).

File management. Divided into 3 components: File Data, Metadata, File System. We write data to our hard drive in form of data blocks. Block storage improves faster handling of data. Metadata contains info about file eg. file size, permissions. Process Management. The process is a program that is executing. The kernel creates processes, efficiently schedules them, and manages how processes are terminated. Memory management. Virtual memory is the combination of hard drive space and RAM that acts like a memory that our processes can use. The kernel also manages input-output. Load drivers to interact with them, data transfer, intercommunication between devices.

Shell is a program that sends text commands to OS to execute. Logs are files that record system events on our computer, just like the system’s diary. On starting OS, BIOS runs a process POST(Power on Self Test) by running some diagnostic tests. The bootloader is a small program that loads the operating system. Next essential system processes and user spaces items are launched.
Virtual Machines(VMs) are just a copy of the real machine.

The remote connection allows us to manage multiple machines from anywhere in the world. Secure Shell (SSH) is a protocol implemented by other programs to securely access one computer from another. An SSH server(software) on the remote machine and SSH client on your machine is required. VPN (a virtual private network) allows you to connect to a private network, like your work network over the internet.

##### Networking

A network is the interconnection of computers. The internet is the physical connection between computers and wires around the world. The web is the information on the internet. Client (mobiles) requests content from servers. Computers on a network have an identifier called an IP Address. A Router connects lots of different devices together and helps route network traffic. A network stack is a set of hardware or software that provides the infrastructure for a computer. Network protocols are a set of rules of how we transfer data in a network. Major is TCP/IP Transmission control protocol and internet protocol. IP is to deliver packets to the right computers and TCP is to deliver information from one network to another. DNS (Domain name system) maps URL to IP Address.

##### Software

How we, users directly interact with our computer. Coding is just translating one language to another. Scripting is coding in a scripting language. Scripts mainly are used to perform a single or limited range task. Application software is a software created to fulfill a specific need like a text editor or a web browser. The system software is used to keep our core system running like OS tools and utilities. Firmware is software that’s permanently stored in a computer component. Software versioning is done to keep track of changes. Apt is the command we use in the ubuntu package manager.

##### Troubleshooting

The ability to diagnose and resolve a problem. Isolating the problem meant to shrink the scope of your problem, in this way we can end up at the root cause. Start with the quickest steps first. Exhibiting empathy, being conscious of your tone, acknowledging the person, developing trust with the user. Proper Documentation of your work is necessary as  It’s vital to document processes and policies not only for yourself but for your teammates that may encounter the same issue.
