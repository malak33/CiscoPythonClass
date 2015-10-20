import locale

locale.setlocale(locale.LC_ALL, '')


class Player:
    """
        Defines a Player and their info (name, salary, year played).
    """
    def __init__(self, f_name, l_name, salary, year_played):
        self._first_name = f_name
        self._last_name = l_name
        self.salary = salary                                # this is invoking the setter property
        self._year_played = year_played

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
        if salary < 0:
            self._salary = 0

    @property
    def year_played(self):
        return self._year_played

    @year_played.setter
    def year_played(self, year_played):
        self._year_played = year_played


def salary_sort(sal_record):
    """
        Used for the key= parameter to sort the player-salary data by salary
        :param sal_record: string value representing a players salary
        :return: integer value for the salary
    """
    salary = 0
    try:
        salary = int(sal_record[4])
    except ValueError:
        pass

    return salary


def get_search_year():
    """ obtain the user's input, disallow non-int values or an empty selection"""
    input_year = 1985
    while True:
        input_year = input('Search salaries for what year?--> ')
        try:
            input_year = int(input_year)
            break
        except ValueError:
            print('Invalid year, try again.')

    return input_year


def get_record_count():
    """  Returns number of records to search for """
    num_records = 10
    try:
        num_records = int(input('Number of records to retrieve (def.=10): '))
    except ValueError:
        print('Retrieving 10 records.')

    return num_records


def retrieve_data(salaries_filename, master_filename, input_year=1985, num_records=10):
    """ Works with the provided files to create the top_sals data structure """
    salaries = []
    players = {}
    top_sals = []

    try:
        # open and work with both files
        with open(salaries_filename) as file_sal, open(master_filename) as file_mast:
            for line in file_sal:                                               # get each salary record
                sal_record = line.strip().split(',')
                try:
                    record_year = int(sal_record[0])
                    if record_year == input_year:
                        salaries.append(sal_record)                                     # load it into a list
                except ValueError:
                    pass

            for line in file_mast:                                              # get each player record
                mast_record = line.strip().split(',')
                players[mast_record[0]] = mast_record                           # load it into a list

            salaries.sort(key=salary_sort, reverse=True)                        # sort the salary records in descending order according to salary

            for top_sal in salaries:                                        # extract necessary data from salaries file
                year = 0
                try:
                    year = int(top_sal[0])                                  # get the year for each salary record
                except ValueError:
                    pass

                try:
                    salary = float(top_sal[4])
                except ValueError:
                    salary = 0

                playerid = top_sal[3]                                       # get the player's id, salary, year
                player_data = players.get(playerid)                         # get the player's name data from the other file data structure
                if player_data:                                             # checks if the player has data in the players dictionary, if not, we ignore them
                    first_name = player_data[13]
                    last_name = player_data[14]
                    p = Player(first_name, last_name, salary, year)
                    top_sals.append(p)                                      # create a list of the player's relevant data
                    if len(top_sals) == num_records:                        # stop after 10 records
                        break
    except IOError as e:
        print('Error: {0}'.format(e))

    return top_sals


def print_report(results_filename, top_sals):
    try:
        with open(results_filename, 'w', encoding='utf8') as f_out:         # write the results to a file
            f_out.write('Results\n')
            f_out.write('{0:<40} {1:<20} {2:<8}\n'.format('Name', 'Salary', 'Year'))
            for player in top_sals:
                name = ' '.join([player.first_name, player.last_name])
                salary = locale.currency(int(player.salary), grouping=True)
                year = player.year_played
                f_out.write('{0:<40} {1:<20} {2:<8}\n'.format(name, salary, year))
    except IOError as e:
        print(e)