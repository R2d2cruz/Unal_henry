from VisualInterface import VisualInterface

switch = False
if switch:
    visual = VisualInterface()
    visual.update()
else:
    from GUI import Constructor
    constructor = Constructor()
    constructor.run()
