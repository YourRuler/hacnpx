import construct
import struct
import Image

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

dbase100C = construct.Struct("dbase100C",
                    construct.String("FileName", 8),        # + 0x00
                    construct.ULInt32("FileSize"),          # + 0x08
                    construct.ULInt32("unk_dword_00"),      # + 0x0C
                    construct.ULInt32("unk_dword_01"),      # + 0x10    // nb 0x14
                    construct.ULInt32("unk_dword_02"),      # + 0x14
                    construct.ULInt32("unk_dword_03"),      # + 0x18    // nb 0x1C
                    construct.ULInt32("unk_dword_04"),      # + 0x1C
                    construct.ULInt32("nb_dbase400"),       # + 0x20
                    construct.ULInt32("pos_dbase400"),      # + 0x24
                             )

entryC = construct.Struct("entryC",
                    construct.String("name", 8),            # + 0x00
                    construct.ULInt32("unk_dword_00"),      # + 0x08
                    construct.ULInt32("offset"),            # + 0x0C
                    construct.ULInt32("unk_dword_02"),      # + 0x10
                            )

dbase400e = construct.Struct("dbase400e",
                    construct.ULInt32("unk_dword_00"),
                    construct.ULInt16("length"),
                    construct.ULInt16("unk_word_01"),
                    construct.String("data", lambda ctx: ctx.length)
                             )

dbase200e = construct.Struct("dbase200e",
                    construct.ULInt16("unk_word_00"),       # + 0x00
                    construct.ULInt32("unk_dword_01"),      # + 0x04
                    construct.ULInt32("unk_dword_02"),      # + 0x08
                    construct.ULInt32("unk_dword_03"),      # + 0x0C
                    construct.ULInt32("unk_dword_04"),      # + 0x10
                             )

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

    def GetWordAt(self, off):
        word = struct.unpack("<H", self.buf[off: off + 2])[0]
        return word

    def GetDwordAt(self, off):
        dword = struct.unpack("<I", self.buf[off: off + 4])[0]
        return dword

    def GetBuffer(self, size):
        data = self.buf[self.pos: self.pos + size]
        self.pos += size
        return data

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

def getdbase200entry(offset, nb):
    b = Buffer(open("DATA/DBASE200.DAT", "rb").read()[offset:])
    size = b.GetDword()
    #print "[+] size = %08X" % size
    flag = b.GetDword()
    width = b.GetWord()
    height = b.GetWord()
    res_buf = uncomp(b, height * width)
    new_buf = ""
    for i in xrange(0, len(res_buf)):
        new_buf += chr(pal_0[ord(res_buf[i])][0]) + chr(pal_0[ord(res_buf[i])][1]) + chr(pal_0[ord(res_buf[i])][2])
    i = Image.frombuffer("RGB", (width, height), new_buf)
    i = i.transpose(Image.FLIP_TOP_BOTTOM)
    i.save("res_dir/%d.png" % nb)
    return (size + 4 + 4)

def getdbase400entry(name, offset):
    if offset == 0:
        return
    buf = open("DATA/DBASE400.DAT", "rb").read()[offset:]
    s =  dbase400e.parse(buf)
    print "[+] unk_dword_00 = %08X" % s['unk_dword_00']
    print "[+] unk_word_01  = %04X" % s['unk_word_01']
    print name + " => " + s['data']

def read_entry_ns(b, nb):
    for i in xrange(0, nb):
        buf = b.GetBuffer(0x14)
        s = entryC.parse(buf)
        #print s
        #if (s['unk_dword_02'] >> 0x18) == 1:
            #print s
        print s
        getdbase400entry(s['name'], s['offset'])

def get_all_d(b, length):
    if length % 2 != 0:
        print "modulo fail"
        sys.exit()
    for i in xrange(0, length / 2):
        print "[+] unk_word_%d = %08X  # + 0x%X" % (i, b.GetWord(), i * 2)

if __name__ == '__main__':
    bdb100 = Buffer(open("DATA/DBASE100.DAT", "rb").read())
    s100 = dbase100C.parse(bdb100.buf)
    print "[+] FileSize     = 0x%08X" % s100['FileSize']
    print "[+] unk_dword_00 = 0x%08X" % s100['unk_dword_00']
    print "[+] unk_dword_01 = 0x%08X" % s100['unk_dword_01']
    print "[+] unk_dword_02 = 0x%08X" % s100['unk_dword_02']
    print "[+] unk_dword_03 = 0x%08X" % s100['unk_dword_03']
    print "[+] unk_dword_04 = 0x%08X" % s100['unk_dword_04']
    print "[+] nb_dbase400  = 0x%08X" % s100['nb_dbase400']
    print "[+] pos_dbase400 = 0x%08X" % s100['pos_dbase400']

    off_1 = s100['unk_dword_02']
    off_2 = s100['unk_dword_04']

    #b.pos = 0 + s['pos_dbase400']
    #read_entry_ns(b, s['nb_dbase400'])

    bdb100.pos = s100['unk_dword_02']

    tsize = 0

    l = []

    for i in xrange(0, s100['unk_dword_01']):
        off = bdb100.GetDword()
        #print "off              = 0x%08X" % off
        length = bdb100.GetWordAt(off)
        unk_word_00 = bdb100.GetWordAt(off + 2)
        flag = bdb100.GetDwordAt(off + 4) & 0xFF
        #print "[+] length       = 0x%08X" % length
        #print "[+] unk_word_00  = 0x%08X" % unk_word_00
        #print "[+] flag         = 0x%08X" % flag
        #if flag & 0x10:
            #print "& 0x10"
            #pass
        #elif flag & 0x20:
            #print "& 0x20"
            #pass
        #elif flag & 0x04:
            #print "& 0x04"
            #pass
            #sys.exit()
        #elif flag & 0x40:
            #print "& 0x40"
            #sys.exit()
            
        ab = bdb100.buf[off + 2: off + 2 + length]
        #save_pos = bdb100.pos
        #bdb100.pos = off
        #ab = bdb100.buf[bdb100.pos: bdb100.pos]
        #print "[+] length       = 0x%08X" % length
        #get_all_d(Buffer(ab), length)
        s = dbase200e.parse(ab)
        #print "[+] unk_word_00  = 0x%04X" % s['unk_word_00']
        #print "[+] unk_dword_01 = 0x%08X" % s['unk_dword_01']
        #print "[+] unk_dword_02 = 0x%08X" % s['unk_dword_02']
        #print "[+] unk_dword_03 = 0x%08X" % s['unk_dword_03']
        #print "[+] unk_dword_04 = 0x%08X" % s['unk_dword_04']
        #print "----"
        l.append(s['unk_dword_03'] * 8)
        if s['unk_dword_03'] * 8 != 0x00:
            tsize += getdbase200entry(s['unk_dword_03'] * 8, i)
        #bdb100.pos = save_pos
    #print "%X" % tsize
