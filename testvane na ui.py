import easygui
rapelist=[]
ime=easygui.enterbox("Vuvedi svoeto ime")
mnenie=easygui.enterbox("Kakvo mislish za supercell")
easygui.msgbox("tvoeto mnenie e: "+ mnenie)
ocenka=easygui.buttonbox("Kolko ni ocenqvate kato firma",choices=['1/5','2/5','3/5','4/5','5/5'])
if ocenka=='5/5':
    easygui.msgbox("Bragodarq nachalnik pechelish 300 gema v brawl stars")
else:
    rapelist.append(ime)
    easygui.msgbox("Added to the rapelist")
