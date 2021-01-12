def convert_to_int(string_object):
    try:
        return int(string_object)
    except ValueError:
        return None

def populate_candidate_dict(dictionary_object, candidate_str, votes_int):
    if candidate_str.lower() not in dictionary_object:
        dictionary_object[candidate_str.lower()] = votes_int
    else:
        dictionary_object[candidate_str.lower()] += votes_int
    
    return dictionary_object

def candidate_loop():
    candidate_input = input("Candidate and votes: ")
    candidate_dict = {}

    while candidate_input != "":
        try:
            candidate, votes = candidate_input.split()
        
            int_votes = convert_to_int(votes)

            if int_votes == None:
                print("Invalid no. of votes!")
            else:
                candidate_dict = populate_candidate_dict(candidate_dict, candidate, int_votes)
        except ValueError:
            print("Invalid no. of votes!")
        
        candidate_input = input("Candidate and votes: ")
    
    return candidate_dict

def get_total_tally(dictionary_object):
    return sum(dictionary_object.values())

def print_candidates(dictionary_object):
    for key, value in sorted(dictionary_object.items()):
        print("{}: {}".format(key, value))

    total_votes = get_total_tally(dictionary_object)
    print("Total no. of votes: {}".format(total_votes))

def main():
    election_dict = candidate_loop()
    print_candidates(election_dict)

main()