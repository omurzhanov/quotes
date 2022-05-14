# Import the necessary module(s).
import textwrap
import json

# This function repeatedly prompts for input until an integer of at least 1 is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        res = input(prompt)
        if res.isnumeric() and int(res) >= 1:
            return int(res)
        


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    
    while True:
        res = input(prompt)
        if res.strip():
            return res.strip()
    

# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    with open('data.txt', 'w') as f:
        data = json.dumps(data_list, indent=4)
        f.write(data)


# Here is where we define function to check if data is empty.
# If the data is empty we do same thing always, we define function to follow DRY principle.
def is_data_empty(data):
    if data == []:
        print("There are no quotes saved.")
        return None
    return True


# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

try:
    f = open('data.txt', 'r')
    data = json.load(f)
    f.close()
except:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the "Quote Catalogue" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 
        
    if choice == 'a':
        # Add a new quote.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        quote = input_something('Enter the quote: ')
        author = input_something('Enter the author\'s name: ')
        year = input('Enter the year (leave blank if unknown): ')
        
        if year != '':
            dict_ = {"quote":quote, "author":author, "year":year, "likes":0, "loves":0}
        else:
            dict_ = {"quote":quote, "author":author, "likes":0, "loves":0}
        
        data.append(dict_)
        save_data(data)
        print("Quote added!")


    
    elif choice == 'l':
        # List the current quotes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        if is_data_empty(data):
            print("List of quotes:")
            for i, d in enumerate(data, 1):
                quote = d['quote']
                if len(quote) > 40:
                    quote = textwrap.shorten(quote, 40)
                try:
                    print(f'  {i}) "{quote}" - {d["author"]}, {d["year"]}')
                except:
                    print(f'  {i}) "{quote}" - {d["author"]}')


    elif choice == 's':
        # Search the current quotes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        
        if is_data_empty(data):
            search_term = input_something('Enter the search term: ').lower()
            print("Search results:")
            no_quote = True
            for i, d in enumerate(data,1):
                if search_term in d['quote'].lower() or search_term in d['author'].lower():
                    quote = d['quote']
                    if len(quote) > 40:
                        quote = textwrap.shorten(quote, 40)
                    try:
                        print(f'  {i}) "{quote}" - {d["author"]}, {d["year"]}')
                    except:
                        print(f'  {i}) "{quote}" - {d["author"]}')
                    no_quote = False
            
            if no_quote:
                print('No results found.')

    elif choice == 'v':
        # View a quote.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if is_data_empty(data):
            index = input_int('Quote number to view: ')
            if index > len(data):
                print("Invalid index number")
            else:
                print(f'  "{data[index - 1]["quote"]}"')
                if "year" in data[index - 1]:
                    print(f'\t- {data[index - 1]["author"]}, {data[index - 1]["year"]}')
                else:
                    print(f'\t- {data[index - 1]["author"]}')
                print(f"\n  This quote has received {data[index-1]['likes']} likes and {data[index-1]['loves']} loves.")

    elif choice == 'd':
        # Delete a quote.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        if is_data_empty(data):
            index = input_int('Quote number to delete: ')
            if index > len(data):
                print("Invalid index number")
            else:
                data.pop(index-1)
                save_data(data)
                print("Quote deleted!")
            

    elif choice == 'q':
        # End the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print('Goodbye!')
        break


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print('Invalid choice')
