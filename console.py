#!/usr/bin/python3
"""Module for console of HBNB project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by handling EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            print(storage.all()[key])
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            objs = storage.all()
        else:
            try:
                objs = {k: v for k, v in storage.all().items()
                        if v.__class__.__name__ == arg}
            except NameError:
                print("** class doesn't exist **")
                return
        print([str(v) for v in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) == 1:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = class_name + '.' + obj_id
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_val = args[3]
            obj = storage.all()[key]
            setattr(obj, attr_name, attr_val)
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
