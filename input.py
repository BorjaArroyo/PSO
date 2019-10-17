# Aux scrypt which retrieves information from the user, this information is stored
# in the list called "result"

def retrieve_mode(result):
    while(True):
        try:
            mode = input("Enter 1 if you want the algorithm to look for maximums "
                 "or 2 if you want to search minmums\n")
            mode = int(mode)

            if(mode != 1 and mode != 2):
                raise ValueError

            result.append(mode)
            break
        except ValueError:
            print("No valid integer in line")

def retrieve_swarm_size(result):
    while(True):
        try:
            size = input("Enter the size of the swarm [100,10000]\n")
            size = int(size)

            if(size < 100 or size > 10000):
                raise ValueError

            result.append(size)
            break
        except ValueError:
            print("No valid integer in line")

def main():
    result = []
    print("Welcome to PSO optimization algorithm")
    retrieve_mode(result)
    retrieve_swarm_size(result)
    return result