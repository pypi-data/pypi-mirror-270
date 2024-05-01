import rwmap._object as object
import rwmap._frame as frame
import rwmap._data.const as const

class Node(object.TObject_One):
    def __init__(self, pos:frame.Coordinate, size:frame.Coordinate = const.COO.SIZE_STANDARD, 
                 name:str = None, warmup:int = -1, reset:int = -1, 
                 id:str = None, alsoacti_s:list[object.TObject_One] = [], 
                 actiBy_s:list[object.TObject_One] = [], deactiBy_s:list[object.TObject_One] = [], 
                 isalltoacti:bool = False):
        upos = frame.Rectangle(pos - size / 2, size)
        object.TObject_One.__init__(self, object.TObject_Type.init_node(), 
                                    object.TObject_Pos.init_rectangle(upos), 
                                    name, object.TObject_Acti.init_acti(id = id, alsoacti_s = alsoacti_s, 
                                                                        actiBy_s = actiBy_s, deactiBy_s = deactiBy_s, 
                                                                        isalltoacti = isalltoacti), 
                                    object.TObject_Time.init_time(warmup = warmup, reset = reset))
