#Winning test cases 

def ifWon3x3(block, input):
    return ((block[7] == input and block[8] == input and block[9] == input) or  
			(block[9] == input and block[6] == input and block[3] == input) or 
            (block[4] == input and block[5] == input and block[6] == input) or 
            (block[1] == input and block[2] == input and block[3] == input) or 
			(block[7] == input and block[5] == input and block[3] == input) or 
            (block[7] == input and block[4] == input and block[1] == input) or  
            (block[8] == input and block[5] == input and block[2] == input) or              
            (block[9] == input and block[5] == input and block[1] == input))  


def ifWon4x4(block, input):
    return ((block[13] == input and block[14] == input and block[15] == input and block[16] == input) or  
            (block[9] == input and block[10] == input and block[11] == input and block[12] == input) or 
			(block[1] == input and block[6] == input and block[11] == input and block[16] == input) or  
            (block[5] == input and block[6] == input and block[7] == input and block[8] == input) or  
			(block[3] == input and block[7] == input and block[11] == input and block[15] == input) or
            (block[1] == input and block[2] == input and block[3] == input and block[4] == input) or  
            (block[1] == input and block[5] == input and block[9] == input and block[13] == input) or
            (block[4] == input and block[7] == input and block[10] == input and block[13] == input) or                
            (block[2] == input and block[6] == input and block[10] == input and block[14] == input) or               
            (block[4] == input and block[8] == input and block[12] == input and block[16] == input))