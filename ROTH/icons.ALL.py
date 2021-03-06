import struct
import os
import Image

# http://www.pythonware.com/products/pil/

pal_0 = [
(0x00, 0x00, 0x00),(0x00, 0x00, 0x00),(0x04, 0x44, 0x20),(0x48, 0x6C, 0x50),
(0x00, 0x50, 0x28),(0x34, 0x64, 0x40),(0x08, 0x3C, 0x1C),(0x00, 0x00, 0x00),
(0x44, 0x30, 0x30),(0x00, 0x00, 0x00),(0x3C, 0x28, 0x24),(0x00, 0x00, 0x00),
(0xBC, 0x80, 0x48),(0x00, 0x00, 0x00),(0x20, 0x10, 0x14),(0x00, 0x00, 0x00),
(0x2C, 0x80, 0x5C),(0x00, 0x00, 0x00),(0x3C, 0x2C, 0x64),(0x00, 0x00, 0x00),
(0x54, 0x2C, 0x0C),(0x00, 0x00, 0x00),(0x64, 0x78, 0x9C),(0x00, 0x00, 0x00),
(0x34, 0x88, 0x5C),(0x00, 0x00, 0x00),(0x44, 0x24, 0x10),(0x00, 0x00, 0x00),
(0x40, 0x3C, 0x38),(0x00, 0x00, 0x00),(0xDC, 0xAC, 0x84),(0x00, 0x00, 0x00),
(0xFC, 0xB0, 0x64),(0xC8, 0x8C, 0x4C),(0x94, 0x68, 0x38),(0x60, 0x44, 0x24),
(0x30, 0x20, 0x10),(0x00, 0x00, 0x00),(0xD0, 0x70, 0x30),(0xB8, 0x60, 0x28),
(0xA0, 0x54, 0x24),(0x88, 0x48, 0x1C),(0x70, 0x3C, 0x18),(0x58, 0x30, 0x10),
(0x40, 0x20, 0x0C),(0x2C, 0x14, 0x08),(0x14, 0x08, 0x04),(0x00, 0x00, 0x00),
(0xAC, 0xC4, 0xE8),(0x40, 0x2C, 0x5C),(0xB4, 0xCC, 0xF0),(0x2C, 0x24, 0x50),
(0x3C, 0x3C, 0x50),(0x1C, 0x1C, 0x28),(0x00, 0x00, 0x00),(0x70, 0x50, 0xBC),
(0x60, 0x44, 0xA4),(0x50, 0x38, 0x8C),(0x44, 0x30, 0x74),(0x34, 0x24, 0x5C),
(0x28, 0x1C, 0x44),(0x18, 0x10, 0x2C),(0x08, 0x04, 0x14),(0x00, 0x00, 0x00),
(0xFC, 0xFC, 0xFC),(0xE8, 0xE8, 0xE8),(0xD8, 0xD8, 0xD8),(0xC8, 0xC8, 0xC8),
(0xB8, 0xB8, 0xB8),(0xA4, 0xA4, 0xA4),(0x94, 0x94, 0x94),(0x84, 0x84, 0x84),
(0x74, 0x74, 0x74),(0x60, 0x60, 0x60),(0x50, 0x50, 0x50),(0x40, 0x40, 0x40),
(0x30, 0x30, 0x30),(0x1C, 0x1C, 0x1C),(0x0C, 0x0C, 0x0C),(0x00, 0x00, 0x00),
(0xBC, 0xD4, 0xF8),(0x00, 0x00, 0x00),(0x9C, 0xB8, 0xEC),(0x00, 0x00, 0x00),
(0xFC, 0xFC, 0x00),(0xE4, 0xE4, 0x00),(0xCC, 0xCC, 0x00),(0xB4, 0xB4, 0x00),
(0x9C, 0x9C, 0x00),(0x88, 0x88, 0x00),(0x70, 0x70, 0x00),(0x58, 0x58, 0x00),
(0x40, 0x40, 0x00),(0x28, 0x28, 0x00),(0x14, 0x14, 0x00),(0x00, 0x00, 0x00),
(0xFC, 0xE0, 0xBC),(0x84, 0x74, 0x64),(0xFC, 0xF0, 0xCC),(0x70, 0x68, 0x60),
(0xF4, 0xCC, 0xA0),(0x00, 0x00, 0x00),(0x00, 0x00, 0x00),(0xFC, 0x00, 0x00),
(0xDC, 0x00, 0x00),(0xBC, 0x00, 0x00),(0x9C, 0x00, 0x00),(0x7C, 0x00, 0x00),
(0x5C, 0x00, 0x00),(0x3C, 0x00, 0x00),(0x1C, 0x00, 0x00),(0x00, 0x00, 0x00),
(0xE8, 0xB8, 0x90),(0xCC, 0xA0, 0x80),(0xB4, 0x8C, 0x70),(0x98, 0x78, 0x5C),
(0x80, 0x64, 0x4C),(0x64, 0x50, 0x3C),(0x48, 0x38, 0x2C),(0x30, 0x24, 0x1C),
(0x14, 0x10, 0x0C),(0x00, 0x00, 0x00),(0xD4, 0x80, 0x6C),(0x68, 0x3C, 0x34),
(0x00, 0x00, 0x00),(0xF4, 0x54, 0x00),(0xD4, 0x48, 0x00),(0xB4, 0x3C, 0x00),
(0x94, 0x30, 0x00),(0x78, 0x28, 0x00),(0x58, 0x1C, 0x00),(0x38, 0x10, 0x00),
(0x1C, 0x04, 0x00),(0x00, 0x00, 0x00),(0x00, 0xAC, 0x5C),(0x00, 0x98, 0x50),
(0x00, 0x84, 0x44),(0x00, 0x70, 0x3C),(0x00, 0x5C, 0x30),(0x00, 0x48, 0x24),
(0x00, 0x34, 0x1C),(0x00, 0x24, 0x10),(0x00, 0x10, 0x04),(0x00, 0x00, 0x00),
(0x38, 0x1C, 0x0C),(0x38, 0x74, 0x58),(0x4C, 0x28, 0x0C),(0x2C, 0x80, 0x5C),
(0x00, 0x20, 0x34),(0x38, 0x84, 0x5C),(0x80, 0x38, 0x14),(0x34, 0x88, 0x5C),
(0xC0, 0x98, 0x7C),(0xDC, 0xAC, 0x84),(0x64, 0x38, 0x10),(0x50, 0x2C, 0x64),
(0x4C, 0x14, 0x00),(0x60, 0x3C, 0x8C),(0x3C, 0x30, 0x24),(0x58, 0x18, 0x84),
(0x54, 0x44, 0x30),(0x6C, 0x44, 0x94),(0x70, 0x5C, 0x44),(0x74, 0x4C, 0x9C),
(0x08, 0x2C, 0x18),(0x84, 0x58, 0xA4),(0x6C, 0x20, 0x00),(0x8C, 0x60, 0xB0),
(0x10, 0x08, 0x24),(0x30, 0x28, 0x50),(0x24, 0x18, 0x30),(0x38, 0x28, 0x4C),
(0x20, 0x14, 0x3C),(0x30, 0x2C, 0x48),(0x3C, 0x38, 0x3C),(0x24, 0x24, 0x24),
(0x60, 0x4C, 0x2C),(0x2C, 0x2C, 0x2C),(0x68, 0x54, 0x3C),(0x18, 0x18, 0x18),
(0x28, 0x10, 0x08),(0x78, 0x60, 0x48),(0x30, 0x18, 0x0C),(0x58, 0x48, 0x40),
(0x8C, 0x70, 0x54),(0x38, 0x2C, 0x40),(0xA4, 0x84, 0x60),(0x2C, 0x28, 0x3C),
(0x54, 0x3C, 0x28),(0x24, 0x28, 0x3C),(0x48, 0x48, 0x44),(0x3C, 0x30, 0x48),
(0x58, 0x58, 0x58),(0x3C, 0x2C, 0x44),(0x34, 0x34, 0x34),(0x50, 0xAC, 0x90),
(0x38, 0x28, 0x24),(0x34, 0x94, 0x88),(0x60, 0x24, 0x04),(0x4C, 0x9C, 0x84),
(0x50, 0x18, 0x00),(0x44, 0x34, 0x80),(0x44, 0x10, 0x00),(0x5C, 0x38, 0x98),
(0x34, 0x18, 0x0C),(0x90, 0x50, 0x24),(0x00, 0x40, 0x20),(0xB0, 0x58, 0x20),
(0x2C, 0x28, 0x44),(0x00, 0x00, 0x7C),(0x80, 0x60, 0x34),(0x80, 0x6C, 0xE4),
(0x78, 0x54, 0x28),(0x8C, 0x80, 0xE8),(0xA8, 0x74, 0x40),(0x8C, 0x9C, 0xF8),
(0xBC, 0xB8, 0xDC),(0x00, 0x00, 0x00),(0x8C, 0xAC, 0xDC),(0x00, 0x00, 0x00),
(0x80, 0xA0, 0xD4),(0x00, 0x00, 0x00),(0x70, 0x8C, 0xD0),(0x00, 0x00, 0x00),
(0x78, 0x90, 0xAC),(0x64, 0x78, 0x9C),(0x00, 0x54, 0x28),(0xA0, 0xE8, 0x54),
(0x30, 0x60, 0x34),(0x10, 0x70, 0x5C),(0x58, 0x68, 0x8C),(0x54, 0x54, 0x90),
(0x50, 0x54, 0x88),(0x54, 0x58, 0x94),(0x44, 0x44, 0x80),(0x60, 0x70, 0x8C),
(0xE8, 0x9C, 0x50),(0xF8, 0xD8, 0x00),(0x18, 0xC8, 0x5C),(0xFC, 0xE4, 0x00),
(0x50, 0xDC, 0x44),(0x14, 0x04, 0x00),(0xF8, 0xC4, 0x24),(0x00, 0x00, 0x00),
(0xE4, 0x84, 0x28),(0x00, 0x00, 0x00),(0xF4, 0x7C, 0x1C),(0x00, 0x00, 0x00),
(0xFC, 0xC8, 0x50),(0x00, 0x00, 0x00),(0xFC, 0xA8, 0x3C),(0x00, 0x00, 0x00),
(0xC0, 0x88, 0x30),(0x00, 0x00, 0x00),(0x48, 0x54, 0x68),(0x70, 0x00, 0xC8)]

class Buffer:
    def __init__(self, buf):
        self.buf = buf
        self.length = len(self.buf)
        self.pos = 0

    def GetByte(self):
        byte = struct.unpack("<B", self.buf[self.pos: self.pos + 1])[0]
        self.pos += 1
        return byte

    def GetWord(self):
        word = struct.unpack("<H", self.buf[self.pos: self.pos + 2])[0]
        self.pos += 2
        return word

    def GetDword(self):
        dword = struct.unpack("<I", self.buf[self.pos: self.pos + 4])[0]
        self.pos += 4
        return dword

def hexdump(src, length=16):
    FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
    lines = []
    for c in xrange(0, len(src), length):
        chars = src[c:c+length]
        hex = ' '.join(["%02x" % ord(x) for x in chars])
        printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or '.') for x in chars])
        lines.append("%04x  %-*s  %s\n" % (c, length*3, hex, printable))
    return ''.join(lines).rstrip('\n')

def createdir(dirname):
    try:
        os.stat(dirname)
    except:
        os.mkdir(dirname)

def uncomp(b, size):
    res_buf = ""
    while size > 0:
        while True:
            r = b.GetByte()
            if r >= 0xF1:
                break
            res_buf += chr(r)
            size = size - 1
            if size < 0:
                return res_buf
        nb = (r + 0x10) & 0xFF
        res_buf += (chr(b.GetByte()) * nb)
        size = size - nb
    return res_buf

def handle_ico(b, pos, nb=0):
    b.pos = pos
    flag = b.GetWord()
    unk_word_01 = b.GetWord()
    width = b.GetWord()
    height = b.GetWord()
    print "[+] flag         = %04X" % flag
    print "[+] unk_word_01  = %04X" % unk_word_01
    print "[+] width        = %04X" % width
    print "[+] height       = %04X" % height
    if flag & 0x01:
        res_buf = uncomp(b, width * height)
        print hexdump(res_buf, width)
        new_buf = ""
        for i in xrange(0, len(res_buf)):
             new_buf += chr(pal_0[ord(res_buf[i])][0]) + chr(pal_0[ord(res_buf[i])][1]) + chr(pal_0[ord(res_buf[i])][2])
        i = Image.frombuffer("RGB", (width, height), new_buf)
        i = i.transpose(Image.FLIP_TOP_BOTTOM)
        i.save("res_dir/%d.png" % nb)
    else:
        print "[-] Unknow flag"

if __name__ == '__main__':
    FILENAME = "ICONS.ALL"
    createdir("res_dir")
    b = Buffer(open(FILENAME, "rb").read())
    for i in xrange(0, 0x79):
        pos = b.GetDword()
        unk_dword_00 = b.GetDword()
        print "[+] pos          = %08X" % pos
        print "[+] unk_dword_00 = %08X" % unk_dword_00
        save_pos = b.pos
        handle_ico(b, pos, i)
        b.pos = save_pos
