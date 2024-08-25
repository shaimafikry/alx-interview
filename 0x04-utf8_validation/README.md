# 0x04. UTF-8 Validation
UTF-8 Encoding Basics:
UTF-8 is a variable-width character encoding that can use 1 to 4 bytes to represent a character.
The first byte in a UTF-8 encoded sequence indicates how many bytes are in the sequence:
1-byte sequence: 0xxxxxxx
2-byte sequence: 110xxxxx 10xxxxxx
3-byte sequence: 1110xxxx 10xxxxxx 10xxxxxx
4-byte sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

### UTF-8 Encoding Rules:
1. **1-Byte Character**:
   - A 1-byte character in UTF-8 must start with `0` (i.e., `0xxxxxxx`).
   - It represents ASCII characters and is valid if the most significant bit is `0`.

2. **Multibyte Characters (2 to 4 bytes)**:
   - The first byte indicates how many bytes are in the sequence:
     - **2-byte sequence**: Starts with `110` (`110xxxxx`).
     - **3-byte sequence**: Starts with `1110` (`1110xxxx`).
     - **4-byte sequence**: Starts with `11110` (`11110xxx`).
   - **Continuation bytes** (i.e., the following bytes in the sequence) must start with `10` (`10xxxxxx`).

### Summary of Rules:
- **1-byte character**: `0xxxxxxx` (first byte starts with `0`).
- **2-byte sequence**: `110xxxxx` (first byte) followed by `10xxxxxx` (continuation byte).
- **3-byte sequence**: `1110xxxx` (first byte) followed by two `10xxxxxx` (continuation bytes).
- **4-byte sequence**: `11110xxx` (first byte) followed by three `10xxxxxx` (continuation bytes).

### To Check if an Integer is Valid UTF-8:
1. **If the integer represents a 1-byte character**:
   - It must start with `0` (`0xxxxxxx`).

2. **If the integer starts a multibyte sequence (2 to 4 bytes)**:
   - The first byte must start with `110`, `1110`, or `11110`, depending on the sequence length.
   - All following bytes in that sequence must start with `10`.

If any byte violates these rules, the sequence is invalid.

### Example:
- `110xxxxx 10xxxxxx` (valid 2-byte sequence)
- `1110xxxx 10xxxxxx 10xxxxxx` (valid 3-byte sequence)
- `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` (valid 4-byte sequence)

Your code should check these conditions to determine if the input data represents a valid UTF-8 encoding.

# Task:
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

### `data = [125, 125, 545, 458] represent the 4 bytes`


# plan:
1 - loop through the list

2- turn the int into binary by using format

3- get only the last 8 digits

4- have a counter to check for the byts num

5- check the first byte, if it has 0 at first nd the num of bytes are 0 continue

6- if it doesnt start with 0, check what it is start with and include it in num of bytes

7- check for the validity if the next byte (Starts with 10) and reduce the num of bytes by one

8- any step not valid would return false inside the loop

9 -  if every byte is vaild meant num of bytes == 0 return true, if not return false



Both `format(467, '#010b')[-8:]` and `bin(467)[2:].zfill(8)` are used to represent the number `467` as an 8-bit binary string, but they do so in slightly different ways. Let's break them down:

### 1. `format(467, '#010b')[-8:]`
- **`format(467, '#010b')`:** Converts the integer `467` to a binary string with a `0b` prefix and pads the result to a total width of 10 characters (including the prefix).
  - For `467`, this would result in the string `'0b0111010011'`.
- **`[-8:]`:** Slices the last 8 characters of the result.
  - For `'0b0111010011'`, slicing the last 8 characters gives `'11010011'`.

### 2. `bin(467)[2:].zfill(8)`
- **`bin(467)`:** Converts the integer `467` to a binary string with a `0b` prefix.
  - For `467`, this would result in the string `'0b111010011'`.
- **`[2:]`:** Removes the `0b` prefix, leaving just the binary digits.
  - For `'0b111010011'`, this gives `'111010011'`.
- **`.zfill(8)`:** Pads the string with zeros on the left to ensure it is at least 8 characters long.
  - For `'111010011'`, this gives `'11101011'`.

### Key Differences:
1. **Padding Length:** 
   - `format(467, '#010b')` ensures the entire string (including the `0b` prefix) is 10 characters long, and the slicing just takes the last 8 digits.
   - `bin(467)[2:].zfill(8)` pads the binary digits themselves to be 8 characters long.

2. **Result for Different Inputs:**
   - For some values, `format` and `bin` might yield different binary representations after padding because `format` accounts for the prefix in its width calculation, whereas `zfill` directly applies padding to the binary digits.

In the case of `467`, both methods produce the same result (`'11010011'`), but the approaches they use differ slightly.
