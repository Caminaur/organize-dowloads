from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
from os.path import exists
import time


class MyHandler(FileSystemEventHandler):

    def stream_control(self, src, filename):
        formatos = ['pdf', 'docx', 'exe', 'zip']
        formatosImagenes = ['jpg', 'jfif', 'png', 'jpeg']
        split = filename.rsplit('.')
        split = split[-1].lower()
        if split in formatos:
            new_destination = destination_folder + "/" + split.upper() + "/"
            self.verify_or_create(new_destination)
            self.move_file(src, new_destination + "/" + filename)
        elif split in formatosImagenes:
            new_destination = destination_folder + "/imagenes/".upper() + split.upper()
            self.verify_or_create(new_destination)
            self.move_file(src, new_destination + "/" + filename)
        else:
            new_destination = destination_folder + "/OTROS".upper()
            self.verify_or_create(new_destination)
            self.move_file(src, new_destination + "/" + filename)

    def move_file(self, src, new_destination):
        try:
            os.rename(src, new_destination)
        except FileExistsError:
            split_string = new_destination.rsplit('.')
            new_destination = split_string[0] + '-1.' + split_string[1]
            self.move_file(src, new_destination)

    def verify_or_create(self, new_destination):
        if exists(new_destination):
            return True
        else:
            try:
                os.mkdir(new_destination)
            except OSError as error:
                print(error)
            finally:
                return True

    def on_modified(self, event):
        descargando = True
        while descargando:
            for filename in os.listdir(folder_to_track):
                if filename.rsplit('.')[1] == 'tmp' or filename.rsplit('.')[1] == 'crdownload':
                    print(filename.rsplit('.', 1))
                    print('esperando a que se complete la descarga')
                    time.sleep(10)
                    descargando = False
            descargando = False

        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            self.stream_control(src, filename)


folder_to_track = r"C:\Usuario\username\Downloads"
destination_folder = r"C:\Users\username\orden"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()
