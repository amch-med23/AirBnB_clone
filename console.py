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
        """ This is a command to exit. """
        return True

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
        """counting the number of elements on a given class"""
        base = storage.all()
        count = 0
        if arg in self.classes:
            for key, value in base.items():
                key_split = key.split('.')
                if key_split[0] == arg:
                    count += 1
            print(count)

    def default(self, line):
        """ this is a defaault method"""
        base = storage.all()
        comando = line.split(".")
        entr = comando
        if len(comando) > 1:
            lista_ins = []
            if comando[0] in self.class_val and comando[1] == "all()":
                HBNBCommand.do_all(self, comando[0])
            elif comando[0] in self.class_val and comando[1] == "count()":
                HBNBCommand.do_count(self, comando[0])
            elif comando[0] in self.class_val and "show" in comando[1]:
                ide = comando[1].split('(')
                ide1 = ide[1].split(')')
                # print(f"{comando[0]}{ide1[0]}")
                HBNBCommand.do_show(self, f"{comando[0]} {ide1[0]}")
            elif comando[0] in self.class_val and "destroy" in comando[1]:
                vari = comando[1].split('(')
                aidi = vari[1].split(')')
                # "id" -> strip -> limpio
                id_cast = aidi[0].strip('"')
                HBNBCommand.do_destroy(self, f"{comando[0]} {id_cast}")
            elif entr[0] in self.class_val and "update" in entr[1]:
                if "{" in comando[1]:
                    ide = entr[1].split("(")[1].split(',')[0].replace('"', "")
                    d = entr[1]
                    d = d.split('(')[1].split('{')[1].split('}')[0].split(',')
                    for i in d:
                        valores = i.split(':')
                        attr = valores[0].replace('"', "").replace("'", "")
                        attr = attr.replace(" ", "")
                        value = valores[1].replace('"', "").replace("'", "")
                        value = value.replace(" ", "")
                        clase = entr[0].strip("''")
                        print(attr)
                        print(value)
                        print(entr[0])
                        print(ide)
                        line = f"{clase} {ide} {attr} {value}"
                        HBNBCommand.do_update(self, line)
                else:
                    f_div = entr[1].split("(")
                    # ['update', '"904a6d22-5860-41c2-8f92-4ca9d47562a9",
                    #  "first_name", "santiago")']
                    coma_div = f_div[1].split(',')
                    # ['"904a6d22-5860-41c2-8f92-4ca9d47562a9"',
                    # ' "first_name"', ' "santiago")']
                    aidi = coma_div[0].strip('"')
                    # ' "first_name"'
                    attr = coma_div[1].strip().strip('"')
                    # "santiago")'
                    arg2 = coma_div[2].split(")")
                    # [' "santiago"', '']
                    val = arg2[0].strip()

                    line = f"{entr[0]} {aidi} {attr} {val}"
                    HBNBCommand.do_update(self, line)
        else:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
