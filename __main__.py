from ProgramObjects.VisualInterface import VisualInterface

switch = False
if switch:
    visual = VisualInterface()
    visual.update()
else:
    from ProgramObjects.GUI import Constructor
    constructor = Constructor()
    constructor.run()
