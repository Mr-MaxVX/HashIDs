# HashFuncID.py - guess the hash function from the number of hex characters
#
# A raw hex hash uses only 0-9 and a-f. Each hex character holds 4 bits,
# so the number of characters tells us the hash size, and the size tells
# us which hash functions could have produced it.

# Length (in hex characters) -> most likely hash function(s)
HASH_TYPES = {
    32:  "MD5 or NTLM (Windows hash)",          # 128-bit
    40:  "SHA-1",                               # 160-bit
    56:  "SHA-224 or SHA3-224",                 # 224-bit
    64:  "SHA-256 or SHA3-256 or BLAKE2s",      # 256-bit
    96:  "SHA-384 or SHA3-384",                 # 384-bit
    128: "SHA-512 or SHA3-512 or BLAKE2b",      # 512-bit
}

# Every character that is allowed in a hex string (upper and lower case)
HEX_CHARS = "0123456789abcdefABCDEF"


def is_hex(text):
    """Return True if every character in text is a hex digit."""
    for ch in text:
        if ch not in HEX_CHARS:
            return False    # found a non-hex character, stop early
    return True


def identify(hash_str):
    """Print the length, bit size and likely type of the given hash."""
    hash_str = hash_str.strip()     # remove spaces/newlines around it
    length = len(hash_str)

    print(f"Characters : {length}")

    # Only raw hex hashes can be identified by length
    if not is_hex(hash_str):
        print("Not a raw hex hash (only 0-9 and a-f allowed).")
        return

    # 1 hex character = 4 bits
    print(f"Bits       : {length * 4}")

    # Look up the length in the table; 'Unknown' if it isn't there
    print(f"Likely type: {HASH_TYPES.get(length, 'Unknown')}")


# Shortest and longest lengths in the table (32 and 128),
# used to reject input that can't be any known hash
MIN_LEN = min(HASH_TYPES)   # 32
MAX_LEN = max(HASH_TYPES)   # 128

# Main loop: keep asking until the user types 'q'
while True:
    h = input("\nWhat is the hash you want to identify its approximate type? (q to quit): ").strip()
    if h.lower() == "q":
        break

    # Too short -> warn and ask again
    if len(h) < MIN_LEN:
        print(f"Warning: hash is too short ({len(h)} chars). Minimum allowed is {MIN_LEN} chars. Try again.")
        continue

    # Too long -> warn and ask again
    if len(h) > MAX_LEN:
        print(f"Warning: hash is too long ({len(h)} chars). Maximum allowed is {MAX_LEN} chars. Try again.")
        continue

    # Length is within range -> identify it
    identify(h)
