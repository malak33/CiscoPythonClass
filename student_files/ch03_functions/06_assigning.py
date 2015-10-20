global_x = 10
def change_global_x():
    global_x = 20               # doesn't change value of global_x

change_global_x()

print(global_x)


# ---------------------------------------------------------------
global_y = 10
def change_global_y():
    global global_y
    global_y = 20               # does change value of global_y!

change_global_y()

print(global_y)


# --------------------------------------------------------------
x = 10
def change():
    print(globals())
    globals()['x'] = 20

change()
print(x)                    # 20
