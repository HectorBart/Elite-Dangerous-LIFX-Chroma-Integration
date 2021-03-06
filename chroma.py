import config

if config.chromaEnable:

    from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid

    KeyboardGrid = ChromaGrid("Keyboard")

    def whiteBright(app):

        # chroma white
        app.Keyboard.setStatic(Colors.WHITE)

    def whiteDim(app):

        # chroma white
        app.Keyboard.setStatic(Colors.WHITE)

    def orange(app):

        # chroma orange
        global KeyboardGrid
        KeyboardGrid.set(hexcolor="#ff9900")
        app.Keyboard.setCustomGrid(KeyboardGrid)
        app.Keyboard.applyGrid()

    def flashGreen(app):

        # chroma green
        app.Keyboard.setStatic(Colors.GREEN)

        # default
        whiteDim(app)

    def flashRed(app):

        # chroma red
        app.Keyboard.setStatic(Colors.RED)

    def flashYellow(app):

        # chroma yellow
        app.Keyboard.setStatic(Colors.YELLOW)

        # default
        whiteDim(app)

    def flashBlue(app):

        # chroma blue
        app.Keyboard.setStatic(Colors.BLUE)

        # default
        whiteDim(app)

else:
    print("Chroma Disabled")
