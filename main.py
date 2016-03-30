from wrappers.lorempixel import LoremPixelWrapper

if __name__ == '__main__':
    lpw = LoremPixelWrapper(width=800, height=400)
    lpw.download()
    print lpw.get_url()
