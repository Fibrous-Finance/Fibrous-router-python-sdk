from fibrous_py import FibrousRouter

def getTokens():
    chainName ='starknet' 
    fibrousClient = FibrousRouter()
    tokens = fibrousClient.supported_tokens(chainName)
    return tokens

if __name__ == "__main__":
    tokens = getTokens()
    print(tokens)