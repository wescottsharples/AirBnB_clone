#!/usr/bin/python3
"""This module is the hbnb console."""
import cmd
from shlex import split
import sys

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """The HBNB console

    Attributes:
        prompt      The prompt to be displayed
        __classes   List of accepted classes
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel",
                 "User",
                 "State",
                 "City",
                 "Amenity",
                 "Place",
                 "Review"]

    def do_create(self, arg):
        """Creates a new instance of specified class"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = eval("{}()".format(arg))
            storage.new(new)
            storage.save()
            print(new.id)

    def do_show(self, arg):
        """Shows attrs of specified instance"""
        args = self.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                print(obj)

    def do_destroy(self, arg):
        """Destroys specified instance"""
        args = self.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Shows attrs of all instances"""
        obj_list = []
        if len(arg) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if arg in key:
                    obj_list.append(storage.all()[key].__str__())
            print(obj_list)

    def do_count(self, arg):
        """Shows count of all instances specified"""
        if arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in storage.all().keys():
                if arg in key:
                    count += 1
            print(count)

    def do_update(self, arg):
        """Update or add attr to specified instance"""
        args = self.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        else:
            key = "{}.{}".format(args[0], args[1])
            arg_type = type(eval(args[3]))
            attr = args[3].strip('\'\"')
            setattr(storage.all()[key], args[2], arg_type(attr))
            storage.all()[key].save()

    def emptyline(self):
        """Prevents program from executing last entered cmd"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def parse(self, arg):
        """Converts arg to tuple of arguments"""
        return tuple(arg.split())

    def default(self, arg):
        args = arg.split('.')
        carg = args[0]
        args = args[1].split('(')
        cmand = args[0]
        if cmand == "all":
            self.do_all(carg)
        elif cmand == "count":
            self.do_count(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
