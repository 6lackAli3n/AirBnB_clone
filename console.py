#!/usr/bin/python3
"""
This module defines the console for the AirBnB clone project.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        ''' exit the program '''
        print("")
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        for pair in args[1:]:
            key, value = pair.split('=')
            setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in [
                "BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
                print("** instance id missing **")
                return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return
            del storage.all()[key]
            storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return
        try:
            class_name = arg.split()[0]
            objs = [str(obj) for obj in storage.all().values()
                    if obj.__class__.__name__ == arg]
            if arg == "User":
                objs.extend(str(obj) for obj in storage.all().values()
                        if isinstance(obj, User))
            if not objs:
                print("** no instance found **")
                return
        except keyError:
            print("** class doesn't exist **")
            return
        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if obj.__class__.__name__ != class_name:
                print("** no instance found **")
                return
            setattr(obj, attr_name, attr_value)
            storage.save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
