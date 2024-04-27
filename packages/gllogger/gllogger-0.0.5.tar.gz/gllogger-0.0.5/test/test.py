from gllogger import gL


if __name__ == "__main__":
    gL.setFunction(lambda text: print(text))
    gL.getLogger(__name__).init("function")

    print("=========================")

    gL.infos("gL.infos")
    gL.warns("gL.warns")
    gL.errors("gL.errors")

    print("=========================")

    _n = "gllogger.test"
    gL.getLogger(_n).infos("gL.getLogger(_n).infos")
    gL.getLogger(_n).warns("gL.getLogger(_n).warns")
    gL.getLogger(_n).errors("gL.getLogger(_n).errors")

    print("=========================")

    gL.getLogger(_n).debug("gL.getLogger(_n).debug")
    gL.getLogger(_n).info("gL.getLogger(_n).info")
    gL.getLogger(_n).warn("gL.getLogger(_n).warn")
    gL.getLogger(_n).warning("gL.getLogger(_n).warning")
    gL.getLogger(_n).error("gL.getLogger(_n).error")
    gL.getLogger(_n).exception("gL.getLogger(_n).exception")

    print("=========================")
