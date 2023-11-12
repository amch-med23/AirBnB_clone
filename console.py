#!/usr/bin/python3
""" This is the console entry point """

import cmd
import json
# importing the models
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
# importing the storage (brigde to models/engine/file_storage)
from models import storage


class HBNBCommand(cmd.Cmd):
    """ this is the command console class """
    # updating the public attribute prompt
    prompt = "(hbnb) "
    classes = ["BaseModel",
               "User",
               "City",
               "Place",
               "Review",
               "Amenity",
               "State"]

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("This is a command to exit.")
        # should return the string as well

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("This is an EndOfFile method that handle Ctrl-D key stroke.")
        # should it be returned?

    # the create command
    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif not (line in self.classes):
            print("** class doesn't exist **")
        else:
            # here we use eval() for instance creation based on
            # the existing clsses in this namespace and the self.classes
            # list
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def help_create(self):
        print("Creates a new instance of the Objects")

    # the show command
    def do_show(self, line):
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            spec_class = args[0] + '.' + args[1]
            if spec_class in all_objects:
                print(all_objects[spec_class])
            else:
                print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of the objects.")

    def do_destroy(self, line):
        args = line.split(" ")
        if not line:
            print("** class name missing **")
        elif not (args[0] in self.classes):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            spec_instance = args[0] + '.' + args[1]
            all_objects = storage.all()
            if not (spec_instance in all_objects):
                print("** no instance found **")
            else:
                del all_objects[spec_instance]
                storage.save()

    def help_destroy(self):
        print("Deletes an instance based on the class name and it's id.")

    def do_all(self, line):
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
        else:
            print(output_list)

    def help_all(self):
        print("Prints all string representation of all instances.")

    def do_update(self, line):
        args = line.split(" ")
        if line is None or len(line) < 1 or line == "":
            print("** class name is missing **")
        elif args[0] not in self.classes:
            print("** class name doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
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

    def help_update(self):
        print("Updates an instance based on the class name and id.")

    # this is to overwrite the emptyline public method
    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
