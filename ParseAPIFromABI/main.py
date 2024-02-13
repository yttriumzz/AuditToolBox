import json


def main():
    f = open("abi.json")
    data = json.load(f)
    f.close()

    abi = json.loads(data["result"])

    read_function = []
    write_function = []
    for interface in abi:
        if interface["type"] == "function":
            if interface["stateMutability"] == "view" or \
                interface["stateMutability"] == "pure":
                read_function.append(interface["name"])
            else:
                write_function.append(interface["name"])

    print("===== Read Function =====")
    for f in read_function:
        print(f)

    print()
    print("===== Write Function =====")
    for f in write_function:
        print(f)


if __name__ == "__main__":
    main()