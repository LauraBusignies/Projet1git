import Utilities
import time

def victory ():
    print("  o              o   __o__       o__ __o    ____o__ __o____     o__ __o        o__ __o    \o       o/ ")
    print(" <|>            <|>    |        /v     v\    /   \   /   \     /v     v\      <|     v\    v\     /v  ")
    print(" < >            < >   / \      />                 \o/         />       <\     / \     <\    <\   />   ")
    print("  \o            o/    \o/    o/                    |        o/           \o   \o/     o/      \o/     ")
    print("   v\          /v      |    <|                    < >      <|             |>   |__  _<|        |      ")
    print("    <\        />      < >    \\                     |        \\\           //    |       \      / \     ")
    print("      \o    o/         |       \                   o          \         /     <o>       \o    \o/     ")
    print("       v\  /v          o        o       o         <|           o       o       |         v\    |      ")
    print("        <\/>         __|>_      <\__ __/>         / \          <\__ __/>      / \         <\  / \   ") 

counter = 0
while counter != 10 :
    counter += 1
    Utilities.clear()
    time.sleep(0.1)
    victory()
    
            