from typing import Tuple

class State():
    def __init__(self, value, name=""):
        self.tag = "STATE"
        self.name = name
        self.value = str(value)
        if type(value) == str:
            self.type = "string"
        elif type(value) == bool:
            self.type = "boolean"
        elif type(value) == int:
            self.type = "int"
        else:
            self.type = "unknown"

class Wrapped():
    def __init__(self, *states: Tuple[State]):
        self.tag = "WRAPPED_OPTION"
        self.states = states
        self.classname = "ghidra.framework.options.Wrapped{}".format(self.__class__.__name__)

class Color(Wrapped):
    def __init__(self, color: str):
        super().__init__(
            State(color, "color")    
        )

class Font(Wrapped):
    def __init__(self, size: int, style: int, family: str):
        super().__init__(
            State(size, "size"),
            State(style, "style"),
            State(family, "family")
        )

class KeyStroke(Wrapped):
    def __init__(self, keyCode: int, modifiers: int):
        super().__init__(
            State(keyCode, "KeyCode"),
            State(modifiers, "Modifiers")
        )

def rgb(r, g, b):
    return -((1<<24) - ((r<<16) + (g<<8) + b))


preferences = {
    "Listing Fields": {
        "Cursor.Cursor Color - Focused": Color(rgb(0xae, 0xaf, 0xad)),
        "Cursor.Cursor Color - Unfocused": Color(rgb(0x39, 0x3d, 0x41)),
        "Cursor.Highlight Cursor Line Color": Color(rgb(0x39, 0x3d, 0x41)),
        "Cursor Text Highlight.Highlight Color": Color(rgb(0x46, 0x4a, 0x4d)),
        "Cursor Text Highlight.Scoped Write Highlight Color": Color(rgb(0x39, 0x3d, 0x41)),
        "Cursor Text Highlight.Scoped Read Highlight Color": Color(rgb(0x39, 0x3d, 0x41)),
        "Selection Colors.Difference Color": Color(rgb(0x0d, 0x50, 0x78)),
        "Selection Colors.Highlight Color": Color(rgb(0x0d, 0x50, 0x78)),
        "Selection Colors.Selection Color": Color(rgb(0x0d, 0x50, 0x78)),
    },
    "Decompiler": {
        "Display.Background Color": Color(rgb(0x1e, 0x1e, 0x1e)),
        "Display.Color Default": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Display.Color for Comments": Color(rgb(0x50, 0x7d, 0x45)),
        "Display.Color for Constants": Color(rgb(0xb2, 0xce, 0xa8)),
        "Display.Color for Current Variable Highlight": Color(rgb(0x39, 0x3d, 0x41)),
        "Display.Color for Function names": Color(rgb(0xde, 0xdc, 0xaa)),
        "Display.Color for Globals": Color(rgb(0x00, 0x99, 0x99)),
        "Display.Color for Highlight Find Mathches": Color(rgb(0x46, 0x4a, 0x4d)),
        "Display.Color for Keywords": Color(rgb(0x34, 0x9d, 0xd7)),
        "Display.Color for Parameters": Color(rgb(0x89, 0xdd, 0xff)),
        "Display.Color for Types": Color(rgb(0x00, 0xcb, 0xb1)),
        "Display.Color for Variables": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Display.Font": Font(14, 0, "DejaVu Sans Mono")
    },
    "Graph": {
        "Function Call Graph.Graph Background Color": Color(-12236470),
        "Function Graph.Default Vertex Color": Color(-14144978),
        "Function Graph.Graph Background Color": Color(-12236470),
        "Function Graph.Edge Color - Conditional Jump ": Color(-10518115),
        "Function Graph.Edge Color - Conditional Jump Highlight": Color(-10510140),
        "Function Graph.Edge Color - Fallthrough ": Color(-5946814),
        "Function Graph.Edge Color - Fallthrough Highlight": Color(-5944240),
        "Function Graph.Edge Color - Unconditional Jump ": Color(-7564224),
        "Function Graph.Edge Color - Unconditional Jump Highlight": Color(-7560616),
    },
    "Search": {
        "Highlight Color for Current Match": Color(rgb(0x42, 0x4e, 0x59)),
        "Highlight Color": Color(rgb(0x67, 0x30, 0x12)),
        "Reference Search.Highlight Match Color": Color(rgb(0x42, 0x4e, 0x59))
    },
    "Listing Display": {
        "Address Color": Color(rgb(0x85, 0x85, 0x85)),
        "Background Color": Color(rgb(0x1e, 0x1e, 0x1e)),
        "Bad Reference Address Color": Color(rgb(0xd4, 0xa6, 0x00)),
        "Bytes Color": Color(rgb(0x81, 0xa2, 0xbe)),
        "Comment, Automatic Color": Color(rgb(0x50, 0x7d, 0x45)),
        "EOL Comment Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Plate Comment Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Post-Comment Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Pre-Comment Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Comment, Repeatable Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Comment, Referenced Repeatable Color": Color(rgb(0x50, 0x7d, 0x45)),
        "Constant Color": Color(rgb(0xb2, 0xce, 0xa8)),
        "Entry Point Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "External Reference, Resolved Color": Color(rgb(0x5e, 0x8d, 0x87)),
        "Field Name Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Flow Arrow, Active Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Flow Arrow, Not Active Color": Color(rgb(0xa0, 0xa0, 0xa0)),
        "Function Call-Fixup Color": Color(rgb(0xb2, 0x94, 0xbb)),
        "Function Name Color": Color(rgb(0xde, 0xdc, 0xaa)),
        "Function Parameters Color": Color(rgb(0x89, 0xdd, 0xff)),
        "Function Auto-Parameters Color": Color(rgb(0x80, 0x80, 0x80)),
        "Function Return Type Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Function Tag Color": Color(rgb(0x85, 0x67, 0x8f)),
        "Labels, Local Color": Color(rgb(0x8c, 0x94, 0x40)),
        "Labels, Non-primary Color": Color(rgb(0x9b, 0x96, 0x32)),
        "Labels, Primary Color": Color(rgb(0x5f, 0x81, 0x9d)),
        "Labels, Unreferenced Color": Color(rgb(0xc5, 0xc8, 0xc6)),
        "Mnemonic Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Mnemonic, Override Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Parameter, Custom Storage Color": Color(rgb(0x85, 0x67, 0x8f)),
        "Parameter, Dynamic Storage Color": Color(rgb(0x5e, 0x8d, 0x87)),
        "Registers Color": Color(rgb(0x9b, 0x96, 0x32)),
        "Separator Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Underline Color": Color(rgb(0xb2, 0x94, 0xbb)),
        "Variable Color": Color(rgb(0xd4, 0xd4, 0xd4)),
        "Version Track Color": Color(rgb(0xb2, 0x94, 0xbb)),
        "XRef Color": Color(rgb(0x8c, 0x94, 0x40)),
        "XRef, Offcut Color": Color(rgb(0x80, 0x80, 0x80)),
        "XRef Read Color": Color(rgb(0x5f, 0x81, 0x9d)),
        "XRef Write Color": Color(rgb(0xde, 0x93, 0x5f)),
        "XRef Other Color": Color(rgb(0xc5, 0xc8, 0xc6)),
        "BASE FONT": Font(14, 0, "DejaVu Sans Mono"),
    },
    "Comments": {
        "Enter accepts comment": State(True)
    },
}
