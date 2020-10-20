COUNTRY = 1
RATING = 2
B_YEAR = 3

def read_file(string_object):
    """ Open a given file string, returns none if file does not exist """
    try:
        return open(string_object, "r")
    except FileNotFoundError:
        return None

def populate_player_dict(file_object):
    """ Reads through a file of chess players and populates a dictionary of players where player names are keys and the value is a tuple: (rank, country, rating, b-year) """
    new_player_dict = {}

    for line in file_object:
        rank, name, country, rating, b_year = line.split(";")
        #The name is a field that is seperated by a comma, so we want to split it further
        last_name, first_name = name.split(",")

        name_key = "{} {}".format(first_name.strip(),last_name.strip())
        value = (int(rank), country.strip(), int(rating), int(b_year))

        new_player_dict[name_key] = value
    
    return new_player_dict

def populate_country_dict(dictionary_object):
    """ Reads through a dictionary of players and returns a dictionary of countries where the country name is the key and the value is a list of players from that country """
    new_country_dict = {}

    for chess_player, chess_player_data in dictionary_object.items():
        country = chess_player_data[COUNTRY]
        if country in new_country_dict:
            name_list = new_country_dict[country]                          #If the country exists in the dictionary we add the player to the list
            name_list.append(chess_player)
        else:
            new_country_dict[country] = [chess_player]                     #If the country does not exist in the dictionary we initialize it with the current player
    
    return new_country_dict

def populate_birth_year_dict(dictionary_object):
    """ Reads through a dictionary of players and returns a dictionary of birth years where the birth years are keys and the values are lists of players """
    new_birth_year_dict = {}

    for chess_player, chess_player_data in dictionary_object.items():
        birth_year = chess_player_data[B_YEAR]
        if birth_year in new_birth_year_dict:
            name_list = new_birth_year_dict[birth_year]
            name_list.append(chess_player)
        else:
            new_birth_year_dict[birth_year] = [chess_player]
    
    return new_birth_year_dict

def calculate_average_rating(players, dictionary_object):
    """ Returns average rating for a given player """
    ratings = [dictionary_object[player][RATING] for player in players]
    average_of_ratings = sum(ratings)/len(ratings)

    return average_of_ratings

def print_country_results(dictionary_object1, dictionary_object2):
    """ Takes two dictionary objects and prints their contents in a readable manner """
    sorted_country_list = sorted(dictionary_object2.items())

    print_country_header()

    for key, players in sorted_country_list:
        average_rating = calculate_average_rating(players, dictionary_object1)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dictionary_object1[player][RATING]
            print("{:>40} {:>10d}".format(player, rating))

def print_birthyear_results(dictionary_object1, dictionary_object2):
    """ Takes two dictionary objects and prints their contents in a readable manner """
    sorted_birthyear_list = sorted(dictionary_object2.items())

    print_birthyear_header()

    for key, players in sorted_birthyear_list:
        average_rating = calculate_average_rating(players, dictionary_object1)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dictionary_object1[player][RATING]
            print("{:>40} {:>10d}".format(player, rating))

def print_country_header():
    header_string = "Players by country:"
    print(header_string)
    print("-"*len(header_string))

def print_birthyear_header():
    header_string = "Players by birth year:"
    print(header_string)
    print("-"*len(header_string))

def main_func():
    """ Main function """
    filename = input("Enter filename: ")
    open_file = read_file(filename)

    if open_file == None:
        print("File {} does not exist".format(filename))
    else:
        player_dict = populate_player_dict(open_file)
        country_dict = populate_country_dict(player_dict)
        birth_year_dict = populate_birth_year_dict(player_dict)
        print_country_results(player_dict, country_dict)
        print_birthyear_results(player_dict, birth_year_dict)

main_func()