import random

def construct():
    global encoder_dict
    global decoder_dict
    global power
    power_list = [x+1 for x in range(10)]
    power = random.choice(power_list)

    alpha_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
                "r","s","t","u","v","w","x","y","z"," ",",","?","!"]
    num_list = [x+(10**power) for x in range(30)]
    encoded = []

    for i in range(30):
        num = random.choice(num_list)
        encoded.append(num)
        num_list.remove(num)

    encoder_dict = {alpha_list[i]:encoded[i] for i in range(len(alpha_list))}
    decoder_dict = {encoded[i]:alpha_list[i] for i in range(len(encoded))}

construct()
while True:
    action = input("You:").lower()
    if "encode" in action:
        string = input("Enter string to be encoded: ").lower()
        output = ""
        for i in string:
            alphabet = encoder_dict.get(i)
            output += str(alphabet)
        print(output)
    elif "decode" in action:
        try:
            string = int(input("Enter string to be decode: "))
            string = str(string)
        except:
            print("Enter valid numericals")
            continue
        output = ""
        num = power + 1
        chunks = [int(string[i:i+num]) for i in range(0, len(string), num)]
        for i in chunks:
            alphabet = decoder_dict.get(i)
            output += str(alphabet)
        print(output)
    elif "construct" in action:
        construct()
    elif "exit" in action:
        exit()