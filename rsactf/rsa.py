import argparse
import math
import sys


def _parse_args():
    parser = argparse.ArgumentParser(description='CTF RSA Generator')
    parser.add_argument("-m", "--message", type=str,
                        help="Message to be encrypted and decrypted")
    parser.add_argument("-p", "--primes", nargs=2, type=int, metavar="prime",
                        help="Load from two big prime numbers")
    parser.add_argument("-e", "--exponent", type=int, metavar="exponent", default=65537,
                        help="Load from exponent")

    return parser, parser.parse_args()

def main():
    parser, args = _parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    e = args.exponent
    if args.message:
        m = int(args.message.encode().hex(), 16)
        print("m:")
        print(m)

    if args.primes:
        n = math.prod(args.primes)
        print("n:")
        print(n)
        phi = (args.primes[0]-1) * (args.primes[1]-1)
        print("phi:")
        print(phi)

        d = pow(e, -1, phi)
        print("d:")
        print(d)

    if args.message and args.primes:
        c = pow(m, e, n)
        print("c:")
        print(c)

if __name__ == "__main__":
    main()
