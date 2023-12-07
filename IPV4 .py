# Function to concatenate name and mask
def pr(name, mask):
    return name + mask

# Function to check if an IP address is correct
def ip_correct_check(octet):
    check = octet.split(".")
    counter = 0
    for i in check:
        if 0 <= int(i) <= 255:
            counter += 1
        else:
            return False
        if counter == 4:
            return True

# Get user input for IP address and validate it
ip_addr = input("Enter IP address of host: ")
while True:
    if ip_correct_check(ip_addr):
        break
    else:
        ip_addr = input("Enter correct IP address of host: ")

# Get user input for IP prefix and validate it
ip_prefix = int(input("Enter IP prefix: "))
while True:
    if 0 <= ip_prefix <= 31:
        break
    else:
        ip_prefix = input("Prefix can be in range [0, 31]: ")

# Determine IP class
ip_list_octet = ip_addr.split(".")
ip_list_octet = [int(i) for i in ip_list_octet]
class_of_ip = None

if int(ip_list_octet[0]) in range(0, 128):
    class_of_ip = "A"
elif int(ip_list_octet[0]) in range(128, 191):
    class_of_ip = "B"
elif int(ip_list_octet[0]) in range(191, 224):
    class_of_ip = "C"
elif int(ip_list_octet[0]) in range(224, 240):
    class_of_ip = "D"
elif int(ip_list_octet[0]) in range(240, 255):
    class_of_ip = "E"

# Determine Public/Private type
type_of_ip = None
if (
    (int(ip_list_octet[0]) == 10)
    or (int(ip_list_octet[0]) == 172 and int(ip_list_octet[1]) in range(16, 32))
    or (int(ip_list_octet[0]) == 192 and int(ip_list_octet[1]) == 168)
):
    type_of_ip = "Private"
else:
    type_of_ip = "Public"

# Convert prefix to binary
mask_bin = int(ip_prefix) * "1" + (32 - int(ip_prefix)) * "0"
mask_bin_list = [mask_bin[i : i + 8] for i in range(0, len(mask_bin), 8)]
mask_dec_list = [int(("0b" + i), 2) for i in mask_bin_list]

# Convert IP address to binary
def ip_in_bin(octet):
    m = str(bin(octet))[2:]
    return m.zfill(8)

bin_ip_list = [ip_in_bin(int(i)) for i in ip_list_octet]

# Calculate Network address in decimal
subnet_decimal_list = [
    int(("0b" + mask_bin_list[i]), 2) & int(("0b" + bin_ip_list[i]), 2)
    for i in range(4)
]

# Calculate Network address in binary
subnet_bin_list = [ip_in_bin(int(i)) for i in subnet_decimal_list]

# Calculate Broadcast address in decimal
broadcast_dec = [
    int(ip_list_octet[i]) if mask_dec_list[i] == 255 else 255
    for i in range(4)
]

# Calculate Broadcast address in binary
broadcast_bin = [ip_in_bin(int(i)) for i in broadcast_dec]

# Calculate First available host in decimal
first_av_host = subnet_decimal_list[:3] + [subnet_decimal_list[3] + 1]

# Calculate Last available host in decimal
last_av_host = [
    subnet_decimal_list[0] + 2 ** (8 - int(ip_prefix)) - 1,
    subnet_decimal_list[1] + 2 ** (16 - int(ip_prefix)) - 1,
    subnet_decimal_list[2] + 2 ** (24 - int(ip_prefix)) - 1,
    subnet_decimal_list[3] + 2 ** (32 - int(ip_prefix)) - 2
]

# Convert First/Last available host to binary
first_bin_list = [ip_in_bin(int(i)) for i in first_av_host]
last_bin_list = [ip_in_bin(int(i)) for i in last_av_host]

# Calculate the number of available hosts
available_number_prom = 32 - ip_prefix
available_number = 2 ** available_number_prom

# Output information
print("IP address: {}/{}".format(ip_addr, ip_prefix))
print("Class of IP address: {}".format(class_of_ip))
print("Address category: {}".format(type_of_ip))
print("Host address (decimal): {}".format(ip_list_octet))
print("Mask (decimal): {}".format(mask_dec_list))
print("Network address (decimal): {}".format(subnet_decimal_list))
print("Broadcast address (decimal): {}".format(broadcast_dec))
print("First available host (decimal): {}".format(first_av_host))
print("Last available host (decimal): {}".format(last_av_host))

print("Host address (binary): {}".format(bin_ip_list))
print("Mask (binary): {}".format(mask_bin_list))
