from web3 import Web3
import json
import base64

infura_url = "https://mainnet.infura.io/v3/56ab69d102bc49c8a2951bbb269d584c"

web3 = Web3(Web3.HTTPProvider(infura_url))

address = "0x78F51427020C5ba128b07E99325D71250B0ed0E1"
abi_string = '''[{"inputs":[{"internalType":"string","name":"_defaultURIPrefix","type":"string"},{"internalType":"address","name":"_provenanceContractAddress","type":"address"},{"internalType":"address","name":"_onChainRendererAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"onChainRenderer","outputs":[{"internalType":"contract IChainRunnersRenderer","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"onChainTokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"provenanceContract","outputs":[{"internalType":"contract IChainRunners","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"prefix","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_onChainRendererAddress","type":"address"}],"name":"setOnChainRenderer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"components":[{"internalType":"uint256","name":"dna","type":"uint256"}],"internalType":"struct ChainRunnersTypes.ChainRunner","name":"runnerData","type":"tuple"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'''
abi = json.loads(abi_string)
contract = web3.eth.contract(address=address, abi=abi)

def get_onchain_token_uri(token_id):
    return contract.functions.onChainTokenURI(int(token_id)).call()

def convert_base64_to_svg(base64_string):
    base64_string = base64_string.split(",")[1]
    json_string = json.loads(base64.b64decode(base64_string))
    with open("runner.svg", "w") as svg_file:
        svg_file.write(json_string["image_data"])
    return "runner.svg"


def get_converted_svg(token_id):
    return convert_base64_to_svg(get_onchain_token_uri(token_id))

