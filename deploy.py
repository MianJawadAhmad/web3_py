from solcx import compile_standard
import json

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)


compiled_sol = compile_standard(
    {
        "language": "solidity",
        "sources": {"SimpleStorage.sol": {"contract": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi, metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0,",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]


# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]


w3 = Web3(Web3.HTTPProvider(os.getenv("RINKEBY_RPC_URL")))
chain_id = 4


# For connecting to ganache
# w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:8545"))
# chain_id = 1337
my_address = "0x643315C9Be056cDEA171F4e7b2222a4ddaB9F88D"
private_key = os.getenv("PRIVATE_KEY")
