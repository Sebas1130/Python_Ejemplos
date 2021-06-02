from proyecto5.stack_based_queue import Queue
from random import randint
from proyecto5.node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title=None) -> None:
        self.title = title
        self.length = randint(5,6)

class MediPlayerQueue(Queue):
    def __init__(self):
        super(MediPlayerQueue, self).__init__()

    def add_track(self,track):
        self.enqueue(track)

    def play(self):
        print(f'count: {self.count}')
        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f'Now playing {current_track_node.data.title}.')

            sleep(current_track_node.data.length)




"""
En el shell de python desde el archivo player_music importamos sus dos clases Track , MediPlayerQueue
despues  agregamos las canciones a la clase Track en la variable track1 y guardamos el primer 
nodo que seria  "white whistle".
Despues instanciamos la clase MediaPlayerQueue en una varibale llamada media_player despues agregamos
esas canciones con el metodo add_track(track1) y le pasamos como parametro la varibale donde se encuentra gurdado el 
elemento. Despues comenzamos a probar los metodos ya desarrollados dentro de la clase MediaPlayerQueue

from player_music import Track,MediPlayerQueue

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")


media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)

media_player.play()
"""