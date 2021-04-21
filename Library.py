# Name: Albert Chap
# Date: April 20, 2021
# Description: This program is a library simulator involving multiple classes. The classes include LibraryItems
#               Patron, and Library. LibraryItems contain classes called Book, Album, and Movie, that inherit from the
#               LibraryItems class.
class LibraryItem:
    """Represents a Library item."""
    def __init__(self, library_item_id, title):
        """Initialized the variables in the LibraryItem class"""
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0

    def get_location(self):
        """Returns the location of the Library Items"""
        return self._location

    def set_location(self, location):
        """Updates location of library item, 'ON_SHELF','ON_HOLD_SHELF', or 'CHECKED_OUT'"""
        self._location = location

    def get_date_checked_out(self):
        """Return the get date checked out"""
        return self._date_checked_out

    def set_date_checked_out(self, check_out_date):
        """ Updates the date a library item is checked out"""
        self._date_checked_out = check_out_date
        # return self._date_checked_out

    def get_checked_out_by(self):
        """Returns who checked out the library item"""
        return self._checked_out_by

    def set_checked_out_by(self, check_out_person):
        """Updates who checked out the library item"""
        self._checked_out_by = check_out_person

    def get_requested_by(self):
        """Returns who requested the item"""
        return self._requested_by

    def set_requested_by(self, requester_id):
        """updates who requests the items"""
        self._requested_by = requester_id

    def get_title(self):
        """Returns the title of the library item"""
        return self._title

    def get_library_item_id(self):
        """Returns the library item ID"""
        return self._library_item_id


class Book(LibraryItem):
    """ represents the Book class that inherits properties from the Library Item class"""
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_check_out_length(self):
        """Returns the checkout length for the Book object"""
        return self._check_out_length

    def get_author(self):
        """ Returns the author of the book"""
        return self._author

    def __repr__(self):
        """ Makes the Book object visible when called"""
        return "Book('{}','{}','{}')".format(self._library_item_id, self._title,self._author)

    def __str__(self):
        """ Makes the checked out list visible"""
        return '[]'.format(self.get_checked_out_by())

class Album(LibraryItem):
    """ represents the Album class that inherits properties from the Library Item class"""

    def __init__(self, library_item_id, title, artist):
        """Initializes the data members in the Album class"""
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_check_out_length(self):
        """Returns the check out length for the Album"""
        return self._check_out_length

    def get_artist(self):
        """ Returns the artist for the Album object"""
        return self._artist

    def __repr__(self):
        """ makes the album object readable to the user"""
        return "Album('{}','{}','{}')".format(self._library_item_id, self._title,self._artist)



class Movie(LibraryItem):
    """ represents the Movie class that inherits properties from the Library Item class"""

    def __init__(self, library_item_id, title, director):
        """Initializes the data members in the Movie class"""
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_check_out_length(self):
        """Returns the checkout length for Movie object"""
        return self._check_out_length

    def get_director(self):
        return self._director

    def __repr__(self):
        return "Movie('{}','{}','{}')".format(self._library_item_id, self._title,self._director)

class Patron:
    """Represents a patron that takes the patron id and name"""

    def __init__(self, patron_id, name):
        """Initializes all the data members in the Patron class"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """Return patron ID"""
        return self._patron_id

    def get_name(self):
        """Return patron Name"""
        return self._name

    def get_fine_amount(self):
        """ Returns the current fine amount """
        return round(self._fine_amount,2)

    def add_library_item(self, library_item):
        """ adds Library item to checked out items """
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """ Removes specified library item from checked out items"""
        self._checked_out_items.remove(library_item)

    def ammend_fine(self, integer):
        """Ammends the fine"""
        self._fine_amount = self._fine_amount + integer
        return self._fine_amount

    def get_checked_out_items(self):
        """Returns the checked_out_items"""
        return self._checked_out_items

    def __repr__(self):
        """returns string representation of the Patron object """
        return "Patron('{}','{}')".format(self._patron_id,self._name)

    def __str__(self):
        """ represents Patron object as a string"""
        return '[]'.format(self.get_checked_out_items())

class Library:
    """This class represents the library"""
    def __init__(self):
        self._current_date = 0
        self._holdings = []
        self._members = []

    def add_library_item(self, library_item_obj):
        """Takes library item object as a parameter and adds it to holdings"""
        self._holdings.append(library_item_obj)

    def add_patron(self,patron_obj):
        """Takes patron objects as a parameter and adds it to the members"""
        self._members.append(patron_obj)

    def lookup_library_item_from_id(self, library_item_id):
        """Returns the LibraryItem object corresponding to the ID parameter, or None if no such LibraryItem is in holdings"""
        for items in self._holdings:
            if items.get_library_item_id() == library_item_id:
                return items
            else:
                None

    def lookup_patron_from_id(self, patron_obj):
        """Returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member"""
        for members in self._members:
            if members.get_patron_id() == patron_obj:
                return members
            else:
                None

    def check_out_library_item(self, patron_id, library_item_id):
        """ Takes in the patron's Id and the respective library item ID to be checked out"""
        if self.lookup_patron_from_id(patron_id) == None:
            return "patron not found"
        elif self.lookup_library_item_from_id(library_item_id) == None:
            return "item not found"
        else:
            check_out_patron = self.lookup_patron_from_id(patron_id)
            check_out_lib_item = self.lookup_library_item_from_id(library_item_id)
            if check_out_lib_item.get_location() == "CHECKED_OUT":
                return "item already checked out"
            elif check_out_lib_item.get_location() == "ON_HOLD_SHELF" and check_out_lib_item.requested_by() != patron_id:
                return "item on hold by other patron"
            else:
                check_out_patron.add_library_item(library_item_id)
                check_out_lib_item.set_checked_out_by(patron_id)
                check_out_lib_item.set_location("CHECKED_OUT")
                check_out_lib_item.set_date_checked_out(0)
                check_out_lib_item.set_requested_by(None)
                return "check out successful"

    def return_library_item(self, return_item_id):
        """Returns the library item back to the library. Updates library item parameters"""
        return_item = self.lookup_library_item_from_id(return_item_id)
        get_patron_id = return_item.get_checked_out_by()
        return_patron = self.lookup_patron_from_id(get_patron_id)
        if self.lookup_library_item_from_id(return_item_id) == None:
            return "item not found"
        else:
            if return_item.get_location() != "CHECKED_OUT":
                return "item already in library"
            elif return_item.get_requested_by() != None:
                return_item.set_location("ON_HOLD_SHELF")
            else:
                return_item.set_location("ON_SHELF")
                return_item.set_checked_out_by(None)
                return_patron. remove_library_item(return_item_id)
                return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """the method takes a patron_id and library item id and returns if the library item has been requested"""
        request_patron = self.lookup_patron_from_id(patron_id)
        request_lib_item = self.lookup_library_item_from_id(library_item_id)
        if request_patron == None:
            return "patron not found"
        elif request_lib_item == None:
            return "item not found"
        elif request_lib_item.get_requested_by() != None:
            return "item already on hold"
        else:
            request_lib_item.set_requested_by(patron_id)
            if request_lib_item.get_location() == "ON_SHELF":
                request_lib_item.set_location("ON_HOLD_SHELF")
            else:
                pass
            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """ This method takes the patron's id and amount_paid in order to """
        paying_patron = self.lookup_patron_from_id(patron_id)

        if paying_patron == None:
            return "patron not found"
        else:
            amount_paid = -1.0 * amount_paid
            paying_patron.ammend_fine(amount_paid)
            return "payment successful"

    def increment_current_date(self):
        """Increments the current day and charges for the overdue library items"""
        self._current_date += 1
        for patron in self._members:
            for library_item in self._holdings:
                if library_item.get_checked_out_by() == patron.get_patron_id():
                    if self._current_date > library_item.get_check_out_length():
                        patron.ammend_fine(0.1)
                    else:
                        pass
                else:
                    pass









