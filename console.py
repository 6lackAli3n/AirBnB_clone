#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for EOF"""
        print("Exit the program by handling EOF")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
