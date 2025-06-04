import pyshark
import binascii
import string
#capture = pyshark.LiveCapture(interface='Wi-Fi')
capture = pyshark.FileCapture("./data/test3.pcap")
#capture.sniff()

for packet in capture:
      if hasattr(packet, 'ip'): # Check if it's a TCP packet
          if (packet.ip.src == "198.6.17.37"):
            #print(f"Destination Port: {packet.tcp.dstport}")
            # Accessing the TCP payload
            if hasattr(packet.tcp, 'payload'):
                hex_split = (packet.tcp.payload.split(':'))
                hex_as_chars = map(lambda hex: chr(int(hex, 16)), hex_split)
                human_readable = ''.join(hex_as_chars)
                # split_headline = (human_readable.split('h:n'))
                # unused_char = (split_headline[0])
                # byte_data = bytes([int(h, 16) for h in hex_split])
                # decoded_string = byte_data.decode('UTF-8',errors='replace')
                # print(decoded_string)
                print(human_readable)
                