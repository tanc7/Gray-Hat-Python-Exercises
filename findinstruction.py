from immlib import *

def main(args):
    imm = Debugger()
    search_code = " ".join(args)
    search_bytes = imm.Assemble( search_code )
    search_results = imm.Search( search_bytes )

    for hit in search_results:
        #retrieve the memory page which this hit exists
        # and make sure its readable
        code_page = imm.getMemoryPageByAddress( hit )
        access = code_page.getAccess( human = True )

        if "execute" in access.lower():
            imm.log( "[*] Found: %s (0x%08x)" % ( search_code, hit ), address = hit )
        return  "[*] Finished searching for instructions, check the Log window."
