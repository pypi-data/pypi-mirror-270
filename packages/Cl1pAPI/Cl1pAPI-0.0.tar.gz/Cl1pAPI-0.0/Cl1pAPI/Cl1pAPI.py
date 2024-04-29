# The cl1p.net API system for Python language 
# Just import it and start using it freely

# Import all needed modules
import requests
from bs4 import BeautifulSoup
import time

# Create the main class
class Cl1pBoard():
    def __init__(self):
        self.Cl1pBoardDefaultURL = "https://cl1p.net/"
        self.Cl1pBoardDefaultAPIURL = "https://api.cl1p.net/"
        self.Cl1pBoardDeleteClipboardURL = "https://cl1p.net/sys/deleteCl1p.jsp"
        self.Cl1pBoardName = ""
        self.DeleteKey = ""
        self.ExpireDate = None
    
    # Define a function which verfies if the clipboard is available
    def isClipboardAvailable(self):
        """
        Verifies if the clipboard is available
        """
        url = self.Cl1pBoardDefaultAPIURL + self.Cl1pBoardName
        r = requests.get(url)
        if r.status_code == 200:
            if r.text.strip() == "":
                return True
        return False

    # Define a function which creates a new clipboard instance
    def createClipboard(self, data:str, timeout:int):
        """
        Create a new clipboard instance with specific data and with timeout time \n

        Timeout is the number of minutes, if you put 0 is gonna exist until is viewed by someone \n
        Data must be a string and it will sended in that format\n

        It finds the time until deletion of clipboard in self.Expire\n
        It find the deletion key in self.DeleteKey
        """

        dataToSend = {
            'ttl': str(timeout),
            'content': data
        }
        url = self.Cl1pBoardDefaultURL + self.Cl1pBoardName
        r = requests.post(url, headers={}, data = dataToSend)

        soup = BeautifulSoup(r.text, 'html.parser')
        DeletionParagraph = soup.find('p', class_='smallerText')
        if DeletionParagraph:
            DeletionTag = DeletionParagraph.find('b')
        try:
            if DeletionTag:
                self.DeleteKey = DeletionTag.get_text().strip()
        except UnboundLocalError:
            pass

        if timeout > 0:
            self.ExpireDate = time.time() + timeout * 60
        else:
            self.ExpireDate = 0    

    # Define a function which gets the data from the clipboard
    def getClipboard(self):
        """
        Gets the data from a clipboard as a string
        """
        url = self.Cl1pBoardDefaultAPIURL + self.Cl1pBoardName
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return False
    
    # Define a function which gets the time to delete from a clipboard
    def deleteClipboard(self):
        """
        Deletes a clipboard based on self.DeleteKey from self.CreateClipboard() 
        """
        payload = {'token': str(self.DeleteKey)}
        r = requests.post(self.Cl1pBoardDeleteClipboardURL, headers={}, data=payload)
        if r.status_code == 200:
            return True
        return False
    