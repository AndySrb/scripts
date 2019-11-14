import argparse

parser = argparse.ArgumentParser(description='Convert between hex,bin and dec')
parser.add_argument('-c','--convert', dest='convert', action='store',
choices={'db','dh','bd','bh','hd','hb'},
help='d= decimal b=binary h=hexdecimal first letter is form which format we are converting from seccond letter is desired format example: py-hexbindec.py -c dh -i 25 this will convert form decimal to hexdecimal')

parser.add_argument('-i',dest='input',action='store',default=argparse.SUPPRESS, type=str, required=True)

args = parser.parse_args()

#print(args.convert)
#print(args.input);

convertTo = args.convert
inputStr = args.input

if convertTo == 'db':
    print(bin(int(inputStr)))
elif convertTo == 'dh':
    print(hex(int(inputStr)))
elif convertTo == 'bd':
    print(int(inputStr,2))
elif convertTo == 'bh':
    print(hex(int(inputStr,2)))
elif convertTo == 'hd':
    print(int(inputStr,16))

