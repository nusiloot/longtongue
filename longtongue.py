"""

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

    @Repository:    https://github.com/edoardottt/longtongue

    @Author:        edoardottt, https://www.edoardoottavianelli.it

"""


# ----- Import external libraries -----
import argparse
import os
import itertools

# ----- Global variables -----

symbols = [
    ",",
    ".",
    "-",
    "_",
    "?",
    "!",
    "@",
    "#",
    "+",
    "*",
    "(",
    ")",
    "%",
    "&",
    "$",
]
directory = "output"
starting_year = 1900
ending_year = 2020
starting_number = 0
ending_number = 99
words_in_passphrase_max = 2  # HIGHLY recommended: don't edit this
items_limit = 200000
print_every = 100  # print update every n items created

# ----- Initial swag -----


def banner():
    print("LONGTONGUE")
    print("")
    print("edoardottt |- github.com/edoardottt")
    print("           |- edoardoottavianelli.it")
    print("GPLv3 License")
    print("------------------------")


def version():
    print("0.1\n")


# ----- Input -----


def get_parser():
    """Create and return a parser (argparse.ArgumentParser instance) for main()
    to use"""
    parser = argparse.ArgumentParser(
        description="Customized Password/Passphrase List inputting Target Info"
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-p", "--person", action="store_true", help="Set the target to be a person."
    )
    group.add_argument(
        "-c",
        "--corporate",
        action="store_true",
        help="Set the target to be a corporate.",
    )
    group.add_argument(
        "-v", "--version", action="store_true", help="Show the version of this program."
    )

    return parser


# ----- Utils -----


def create_output_folder():
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(input_filename):

    create_output_folder()
    filename = directory + "/" + input_filename

    if os.path.exists(filename):
        choice = input(
            "{} already exists. Do you want to overwrite? (y/n):".format(input_filename)
        )
        if str(choice).lower() == "n":
            exit(1)
        # if choice == y: ====> go forward. The file's content will be flushed and overwritten
    else:
        os.mknod(filename)


def prepare_keywords(str_input):
    """
    It outputs None if blank
    It outputs an array if valid
    """
    if not str_input or len(str_input) == 0:
        return None
    temp = str_input.split(",")
    result = []
    for elem in temp:
        if elem.strip() != "":
            result.append(elem.strip())
    return result


def create_subsets(list_input, k):
    """
    It returns all the subsets (length k) of list_input
    """
    unique_words = set(list_input)
    subsets = itertools.combinations(unique_words, k)

    return subsets


# ----- Person -----


class Person:
    def __init__(
        self,
        name=None,
        middle_name=None,
        surname=None,
        nickname=None,
        username=None,
        age=None,
        birth_day=None,
        birth_month=None,
        birth_year=None,
        email=None,
        birth_place=None,
        first_pet=None,
        second_pet=None,
        favourite_band=None,
        person_keywords=None,
    ):

        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.nickname = nickname
        self.username = username
        self.age = age
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.email = email
        self.birth_place = birth_place
        self.first_pet = first_pet
        self.second_pet = second_pet
        self.favourite_band = favourite_band
        self.person_keywords = person_keywords


def person():
    print("person\n")
    target = input_person()

    # output filename
    if target.name and target.name != "":
        create_output_file(target.name + "-" + target.surname + ".txt")
    else:
        create_output_file("longtongue-output.txt")


def input_person():

    target = Person()

    print(
        "Enter all the information you know. Leave blank and hit enter if you don't know.\n"
    )
    target.name = input("Name: ")
    target.middle_name = input("Middle Name: ")
    target.surname = input("Surname: ")
    target.nickname = input("Nickname: ")
    target.username = input("Username: ")
    target.age = input("Age: ")
    target.birth_day = input("Birth day: ")
    target.birth_month = input("Birth month: ")
    target.birth_year = input("Birth year: ")
    target.email = input("Email: ")
    target.birth_place = input("Birth place: ")
    target.first_pet = input("First pet: ")
    target.second_pet = input("Second pet: ")
    target.favourite_band = input("Favourite Band: ")

    person_keywords = input("Useful keywords (separated by comma): ")

    target.person_keywords = prepare_keywords(person_keywords)

    return target


# ----- Corporate -----


class Corporate:
    def __init__(
        self,
        name=None,
        birth_year=None,
        corporate_keywords=None,
    ):

        self.name = name
        self.birth_year = birth_year
        self.corporate_keywords = corporate_keywords


def corporate():
    print("corporate\n")
    target = input_corporate()

    # output filename
    if target.name and target.name != "":
        create_output_file(target.name + ".txt")
    else:
        create_output_file("longtongue-output.txt")


def input_corporate():

    target = Corporate()

    print(
        "Enter all the information you know. Leave blank and hit enter if you don't know.\n"
    )
    target.name = input("Name: ")
    target.birth_year = input("Birth year: ")

    corporate_keywords = input("Useful keywords (separated by comma): ")
    target.corporate_keywords = prepare_keywords(corporate_keywords)

    return target


# ----- Main function -----


def main():

    banner()

    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        version()
    elif args.corporate:
        corporate()
    elif args.person:
        person()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
