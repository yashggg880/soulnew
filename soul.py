byte_value = input("Enter the byte value (e.g., 90): ")
total_kb = float(input("Enter the total size in KB: "))
total_bytes = int(total_kb * 1024)
hex_byte = f"\\x{byte_value}"
repeat_count = total_bytes
grouped_output = ','.join([f'"\\x{byte_value},\\x{byte_value}"'] * repeat_count)

with open("soul.txt", "w") as file:
    file.write(grouped_output)

print("Data saved to soul.txt successfully! By @SOULCRACKS")