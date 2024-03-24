#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        ''' exit the program '''
        return True

    def help_EOF(self):
        ''' help EOF'''
        print("EOF command to exit the program\n")

    def help_quit(self):
        ''' help quit '''
        print("Quit command to exit the program\n")

    def do_quit(self, arg):
        ''' quit interpreter '''
        return True

    def emptyline(self):
        ''' do nothing with empty line '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
