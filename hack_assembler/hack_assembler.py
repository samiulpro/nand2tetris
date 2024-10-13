comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }

dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }


jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
    }

symbol_table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7,
    "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576
}


with open('C:/Users/sami/Documents/Nand2Tetris/originals/projects/6/max/Max.asm', 'r') as asm_file:
    lines = asm_file.readlines()
    
    #Cleaning comments
    cleaned_lines = []
    for i in lines:
        i = i.strip()
        if not i.startswith("//") and i:
            cleaned_lines.append(i)



#a instruction handling
def a_instruction(cmd):
    binary_representation = f"0{format(cmd, '015b')}"
    return binary_representation

#symbol handling
next_variable_address = 16

def add_symbol(symbol, address):
    """ Add a new symbol to the symbol table. """
    if symbol not in symbol_table:
        symbol_table[symbol] = address
    
def resolve_symbol(symbol):
    """ Resolves symbols to their addresses (variables or labels). """
    global next_variable_address
    if symbol.isdigit():
        return int(symbol)  # If it's a number, just return the number
    
    # If the symbol is not already in the table, treat it as a variable and assign it a memory address
    if symbol not in symbol_table:
        symbol_table[symbol] = next_variable_address
        next_variable_address += 1
    return symbol_table[symbol]


#c instruction handling
def c_instruction(cmd):
    compu = "0000000"
    destu = "000"
    jumpu = "000"
    parts = cmd.split(";")
    comp_cmd = parts[0]
    
    # Handle comp part (this is mandatory)
    if "=" in comp_cmd:
        dest_cmd, comp_cmd = comp_cmd.split("=")
        if dest_cmd in dest:
            destu = dest[dest_cmd]
    
    if comp_cmd in comp:
        compu = comp[comp_cmd]
    
    # Handle jump part (optional)
    if len(parts) > 1:
        jump_cmd = parts[1]
        if jump_cmd in jump:
            jumpu = jump[jump_cmd]
    
    # Combine into the full C-instruction binary
    c_out = "111" + compu + destu + jumpu
    return c_out

def first_pass(lines):
    line_number = 0
    for line in lines:
        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]
            add_symbol(label, line_number)
        else:
            line_number += 1  # Only count non-label lines
            
            
first_pass(cleaned_lines)

final_lines = []
line_number = 0    
for i in cleaned_lines:
    if i.startswith("@"):
        if i[1:].isdigit():
            print(a_instruction(int(i[1:])))
            final_lines.append(str(a_instruction(int(i[1:]))))
        else:
            symbol = i[1:]
            address = resolve_symbol(symbol)
            print(a_instruction(address))
            final_lines.append(str(a_instruction(address)))
    elif not (i.startswith("(") and i.endswith(")")):
        print(c_instruction(i))
        final_lines.append(c_instruction(i))
        
    line_number +=1
    
    
with open("Max.hack", "a") as hack_file:
    for line in final_lines:
        hack_file.write(line+'\n')
    
    print("Successful")