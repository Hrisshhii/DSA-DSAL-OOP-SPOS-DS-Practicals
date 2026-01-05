MNT = {}
MDT = {}
ALA = {}
def pass_1(programlines):
    i = 0
    while i < len(programlines):
        parts = programlines[i].split()
        if parts[0] == "MACRO":
            macro_name = parts[1]
            MNT[macro_name] = len(MDT)
            ALA[macro_name] = []
            # Collect formal parameters
            for arg in parts[2:]:
                if arg.startswith('&'):
                    ALA[macro_name].append(arg)
            # Collect macro body
        mdt_entry = []
        i += 1
        while i < len(programlines) and programlines[i] != "MEND":
            mdt_entry.append(programlines[i])
            i += 1
        MDT[macro_name] = mdt_entry
        i += 1
    return MDT, MNT, ALA

def pass_2(programlines):
    output = []
    i = 0
    while i < len(programlines):
        parts = programlines[i].split()
        if parts and parts[0] in MNT:
            macro_name = parts[0]
            actualParams = parts[1:]
            formalParams = ALA[macro_name]
            paramMap = {formalParams[j]: actualParams[j] for j in range(len(formalParams))}
            for mdt_line in MDT[macro_name]:
                expanded_line = mdt_line
                for formal in formalParams:
                    expanded_line = expanded_line.replace(formal, paramMap[formal])
            output.append(expanded_line)
        elif parts and parts[0] not in ["MACRO", "MEND"]:
            output.append(programlines[i])
        i += 1 
    return output
 # Example usage

programlines = [
    "MACRO INCR &ARG1 &ARG2",
    "LOAD &ARG1",
    "ADD &ARG2",
    "STORE &ARG1",
    "MEND",
    "START",
    "INCR 1 2",
    "END"
]
MDT, MNT, ALA = pass_1(programlines)
expanded_code = pass_2(programlines)
print("MNT:", MNT)
print("MDT:", MDT)
print("ALA:", ALA)
print("\nExpanded Code:")
for line in expanded_code:
    print(line)