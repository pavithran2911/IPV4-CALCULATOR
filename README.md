# IPV4-CALCULATOR

The IP Address Analysis Tool is a Python script that provides information about an IP address, including its class, public or private type, network details, and available hosts. This tool is useful for understanding the characteristics of an IP address and its associated subnet.

## Features

- **IP Address Details:** Determine the class and public/private type of the given IP address.
  
- **Subnet Information:** Calculate network and broadcast addresses, subnet mask in both binary and decimal formats.

- **Available Hosts:** Find the first and last available hosts within the subnet.

## Usage

1. Run the script using Python.
2. Enter the IP address of the host when prompted.
3. Enter the IP prefix (subnet mask) when prompted.
4. Review the detailed information about the IP address and its subnet.

## Example

### Input
Enter IP address of host: 192.168.1.10
Enter IP prefix: 24

### Output
IP address: 192.168.1.10/24
Class of IP address: C
Address category: Private
Host address (decimal): [192, 168, 1, 10]
Mask (decimal): [255, 255, 255, 0]
Network address (decimal): [192, 168, 1, 0]
Broadcast address (decimal): [192, 168, 1, 255]
First available host (decimal): [192, 168, 1, 1]
Last available host (decimal): [192, 168, 1, 254]
...

## Contrubuting
If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.
