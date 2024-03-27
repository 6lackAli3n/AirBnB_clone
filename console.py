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
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    ''' HBNB class contains entry point '''

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        ''' exit the program '''
        print()
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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {
                "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {
                "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        all_objs = storage.all()
        key = class_name + "." + obj_id
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

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
        else:
            try:
                class_name = arg.split()[0]
                if class_name not in [
                        "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                    print("** class doesn't exist **")
                    return
                if class_name == "User":
                    objs = [str(obj) for obj in storage.all().values() if isinstance(obj, User)]
                else:
                    objs = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == class_name]
                if not objs:
                    print("** no instance found **")
                    return
            except IndexError:
                print("** class name missing **")
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
        except Exception as e:
            print(e)

    def do_count(self, arg):
        """Count the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in {
                "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(class_name + "."))
        print(count)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
