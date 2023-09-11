import socket

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        birth_year = currentYear - self.year
        print(f'Your age is {birth_year}')

    def listAnniversaries(self):
        current_year = 2022  # Assuming today is year 2022
        years_since_birth = current_year - self.year
        anniversaries = [i for i in range(10, years_since_birth + 1, 10)]
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        repeated_first_two_chars = year_str[:2] * n
        odd_chars = year_str[::2]
        modified_year = repeated_first_two_chars + (odd_chars * n)
        return modified_year

    @staticmethod
    def connectTcp(host, port):
        try:
            # Create a TCP IPv4 socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the specified host and port
            sock.connect((host, port))
            
            # Close the connection
            sock.close()
            
            # Return True if the connection was established correctly
            return True
        except Exception as e:
            # Handle exceptions and return False if the connection cannot be established
            return False

# Testing the connectTcp method
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
