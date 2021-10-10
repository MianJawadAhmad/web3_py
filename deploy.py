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
