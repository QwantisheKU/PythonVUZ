import struct
# import pprint

D_SIZE = 8 + 8 + 8
C_SIZE = 4 + 2 + 4 + 4
B_SIZE = 2 + 2 + 2 + 4*5 + 8 + 2
A_SIZE = 4 + 2 + 2 + 8 + 1 + B_SIZE

def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>dQq', d_bytes)
    return {
        'D1': d_parsed[0],
        'D2': d_parsed[1],
        'D3': d_parsed[2]
    }

def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>IHfi', c_bytes)
    c1_bytes = byte_string[c_parsed[1]:c_parsed[1] + c_parsed[0]]
    c1_parsed = struct.unpack('>' + 'b' * c_parsed[0], c1_bytes)
    return {
        'C1':list(c1_parsed),
        'C2': c_parsed[2],
        'C3': c_parsed[3]
    }

def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>HHHfffffBBBBBBBBH', b_bytes)
    b2_parsed = struct.unpack('>' + 'I' * b_parsed[1],byte_string[b_parsed[2]:b_parsed[2] + b_parsed[1] * 4])
    b2_list = [parse_c(addr, byte_string) for addr in b2_parsed]
    return {
        'B1': b_parsed[0],
        'B2': b2_list,
        'B3': list(b_parsed[3:8]),
        'B4': list(b_parsed[8:16]),
        'B5': parse_d(b_parsed[16], byte_string)
    }

def parse_a(offset, byte_string):
    a1234_bytes = byte_string[offset:offset + 17]
    a1234_parsed = struct.unpack('>IHHQB', a1234_bytes)
    a2_bytes = byte_string[a1234_parsed[2]:a1234_parsed[2] + a1234_parsed[1]]
    a2_parsed = struct.unpack('>' + 'c' * a1234_parsed[1], a2_bytes)
    a5_parsed = parse_b(offset + 17, byte_string)
    return {
        'A1': a1234_parsed[0],
        'A2': b''.join(list(a2_parsed)).decode('utf-8'),
        'A3': a1234_parsed[3],
        'A4': a1234_parsed[4],
        'A5': a5_parsed
    }

def f31(byte_string):
    return parse_a(5, byte_string)

# pprint.pprint(f31((b'UWJG\xc8\xbf\xd9\xb9\x13\x00\x06\x00:\x9e>V\xaeK\xe1\xcd\x13T\xd8\xfc'
# b'\x00\x02\x00a?=\xd5P\xbd9\x9f/\xbf`N\xea\xbf\x149\x96=2\x13\xd7\xc3iFG'
# b'\xd2A\xe2\xa3\x00ifsidxm>\x14\x96\x00\x00\x00\x03\x00@\xba1U\xe7\x17\xbf7'
# b'\xc953\x00\x00\x00\x02\x00Q?{v\x88Y\x12\xf6\xed\x00\x00\x00C\x00\x00\x00'
# b"S?\xde\xfc\x1d\x81\xb1\x1aXM,tq\xfb\xf4\x0c\xdd\xe50\xb4G'o=.")))

# pprint.pprint(f31((b'UWJG\xc8x8\x06\xf0\x00\x04\x00:\x19P\x10J\xb6\x17\x0f\nv\x05\x87'
# b'\x00\x03\x00n?\x1a\x19=\xbe\xb2\xefh\xbfiv\x03?3\x81\xb9\xbf\n\xc3='
# b'\xdfM\xff\xde\xa6R\xad\xf5\x00zppsn\xbbo\x00\x00\x00\x02\x00>\xbfSz6\x05\xfc'
# b'$p\xa9f\x00\x00\x00\x02\x00N\xbf)D\xbf\xf7\x0f\xdf19\x97\x00\x00\x00\x02'
# b'\x00^? \x8b\xbc\xaf\x19\xe3\x8e\x00\x00\x00@\x00\x00\x00P\x00\x00'
# b'\x00`\xbf\xe7\r5\xfe\xec\xcfV@E\xa2\xc9\xa9\x94w\xac!\x9cO\xe6\xf5\x98'
# b'\x99\xfb')))