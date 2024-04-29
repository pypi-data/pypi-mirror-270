'''
    File: voting_methods.py
    Author: Wes Holliday (wesholliday@berkeley.edu) and Eric Pacuit (epacuit@umd.edu)
    Date: November 6, 2021
    Update: January 15, 2023
    
    The VotingMethodProperties class to encapsulate properties of voting methods.
'''


class VotingMethodProperties:
    """
    Class to encapsulate properties of voting methods.

    Attributes:
        condorcet_consistent (bool): Indicates if the voting method always elects a Condorcet winner when one exists.
    """
    def __init__(self, condorcet_winner=False, **kwargs):
        self.condorcet_winner = condorcet_winner
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        properties = [f"{key}: {'Satisfied' if value else 'Violated'}" for key, value in self.__dict__.items()]
        return "\n".join(properties)
