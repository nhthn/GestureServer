import argparse
import io
import qrcode
import common

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--invert", action="store_true")
    args = parser.parse_args()

    qr = qrcode.QRCode()
    qr.add_data(f"http://{common.PRIVATE_IP_ADDRESS}:5000/")
    qr.make(fit=True)
    f = io.StringIO()
    qr.print_ascii(out=f, invert=args.invert)
    f.seek(0)
    print(f.read())
