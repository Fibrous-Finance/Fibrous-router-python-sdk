from fibrous_sdk_py import FibrousRouter

def getTokens():
    chainName ='scroll' 
    fibrousClient = FibrousRouter()
    tokens = fibrousClient.supported_tokens(chainName)
    return tokens

if __name__ == "__main__":
    tokens = getTokens()
    print(tokens)