def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # For each integer in the data list
    for d in data:
        # Set the mask to check the first two bits
        mask = 1 << 7

        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading ones to determine the number of bytes
            while mask & d:
                num_bytes += 1
                mask = mask >> 1

            # 1-byte characters
            if num_bytes == 0:
                continue

            # Invalid UTF-8 encoding if the first two bits are either 10 or the number of bytes is more than 4
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the first two bits are 10
            if not (d & 1 << 7 and not (d & 1 << 6)):
                return False

        # Decrement the count of bytes
        num_bytes -= 1

    # If all characters are valid UTF-8, return True
    return num_bytes == 0

# Example usage
data = [197, 130, 1]
print(validUTF8(data))  # Output: True
