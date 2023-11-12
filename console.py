#!/usr/bin/python3
""" This is the console entry point, this class uses cmd model """

from itertools import count
import cmd
import json
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models import storage
from datetime import datetime
import os


class HBNBCommand(cmd.Cmd):
    """ this is the command console class """
    prompt = '(hbnb) '
    classes = ["BaseModel",
               "User",
               "City",
               "Place",
               "Review",
               "Amenity",
               "State"]

    def do_quit(self, line):
        """ this quits """
        return True

    def help_quit(self):
        """ this help output """
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """ This is an EndOfFile method that handle Ctrl-D key stroke. """
        return True

    def emptyline(self):
        """ this is an overwrite """
        pass

    def do_create(self, line):
        """ Creates a new instance of the Objects """
        if line is None:
            print("** class name missing **")
            return
        elif not (line in self.classes):
            print("** class doesn't exist **")
            return
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of the objects """
        args = line.split(" ")
        if not line:
            print("** class name missing **")
            return
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            all_objects = storage.all()
            spec_class = args[0] + '.' + args[1]
            if spec_class in all_objects:
                print(all_objects[spec_class])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and it's id """
        args = line.split(" ")
        if not line:
            print("** class name missing **")
            return
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            spec_instance = args[0] + '.' + args[1]
            all_objects = storage.all()
            if not (spec_instance in all_objects):
                print("** no instance found **")
                return
            else:
                del all_objects[spec_instance]
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances. """
        all_objects = storage.all()
        output_list = []
        all_obj_list = list(all_objects.values())
        for obj in all_obj_list:
            output_list.append(str(obj))
        if line:
            if line in self.classes:
                rec_string = '[' + line + ']'
                selection_list = []
                for obj in all_obj_list:
                    if obj.__class__.__name__ == line:
                        selection_list.append(str(obj))
                print(selection_list)
            else:
                print("** class doesn't exist **")
                return
        else:
            print(output_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id """
        args = line.split(" ")
        if line is None or len(line) < 1 or line == "":
            print("** class name is missing **")
            return
        elif args[0] not in self.classes:
            print("** class name doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            all_objects = storage.all()
            instance = args[0] + '.' + args[1]
            if instance not in all_objects:
                print("** no instance found **")
            else:
                for key, value in all_objects.items():
                    val = args[3]
                    if '"' in val:
                        val = val.strip('"')
                    if instance == key:
                        setattr(value, args[2], val)
                        storage.save()

    def do_count(self, arg):
        """
        count number of instances by class
        """
        counter = 0

        new_arg = arg.split(" ")
        if new_arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_list = storage._FileStorage__objects.items()
        for key, value in new_list:
            temp_key = str(key)
            new_key = temp_key.split(".")
            if new_key[0] == new_arg[0]:
                counter = (counter + 1)
        print(counter)

    def help_count(self):
        """
        counts the number of instances of a class
        """
        print("count <class>")

    def default(self, line):
        '''
        Advanced
        '''
        _cmd = storage.all()
        if '.' in line:
            cmd_parse = line.split('.')
            class_name = cmd_parse[0]
            method_name = cmd_parse[1]
            if class_name in self.classes:
                if method_name == 'all()':
                    self.do_all(class_name)
                if method_name == 'count()':
                    self.do_count(class_name)
                if method_name[0:5] == 'show(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    arg = class_name + ' ' + show_id
                    print(arg)
                    self.do_show(arg)
                if method_name[0:8] == 'destroy(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    arg = class_name + ' ' + show_id
                    self.do_destroy(arg)
                if method_name[0:7] == 'update(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    show_att_name = method_name2[3]
                    show_att_val = method_name2[5]
                    arg = class_name + ' ' + show_id +\
                        ' ' + show_att_name + ' ' + show_att_val
                    print(arg)
                    self.do_update(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
