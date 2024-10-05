#! /usr/bin/env python3
import click
import qrcode


def generate_qr(input_string, output):
    qr_img = get_qr_image(input_string)
    qr_img = qr_img.convert("RGBA")
    qr_img.save(output)
    click.echo(f"QR code with Wi-Fi symbol has been saved as {output}")
    qr_img.show()



def get_qr_image(input_string):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction for image overlay
        box_size=10,
        border=1,
    )
    qr.add_data(input_string)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    return qr_img


@click.command()
@click.option("-s", "--ssid", prompt="Enter the SSID of the Wi-Fi network")
@click.option("-p", "--password", prompt="Enter the password of the Wi-Fi network")
@click.option("-o", "--output", prompt="Enter the output file name")
def generate_wifi_qr_code(ssid: str, password: str, output: str):
    input_string = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    generate_qr(input_string, output)



if __name__ == '__main__':
    generate_wifi_qr_code()

