import time
import sys
import os


class colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"


def victimScan():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print("\n{}Victim Scanned the QR!{}".format(colors.GREEN, colors.END))
    time.sleep(2)
    print("\nCollecting Basic Information.....\n ")


def fake_loading():
    print("Loading:", end=" ")
    for i in range(101):
        sys.stdout.write("\r")
        sys.stdout.write(
            "{}[{}%0s] {}%[{}s]".format(
                colors.YELLOW, colors.RED, "=" * i, i, colors.END
            )
        )
        sys.stdout.flush()
        time.sleep(0.01)

    print("{}\nLoading complete!{}".format(colors.GREEN, colors.END))
    time.sleep(1.5)


def fake_credentials():
    os.system("cls" if os.name == "nt" else "clear")
    width = 69  # Width of the box, subtracting one '='
    line = "=" * width
    print("\n" + line)
    time.sleep(0.3)
    print("{:<41}".format("Address: Punta OC, Leyte, Philippines"))
    time.sleep(0.2)
    print("{:<41}".format("Device: LG MODEL"))
    time.sleep(0.2)
    print("{:<41}".format("School: Eastern Visayas State University OC"))
    time.sleep(0.2)
    print("{:<41}".format("Age: 18"))
    time.sleep(0.2)
    print("{:<41}".format("Email: kimjoshualopez30@gmail.com"))
    time.sleep(0.2)
    print("{:<41}".format("Phone: +09518332554"))
    time.sleep(0.2)
    print("{:<41}".format("Occupation: Student"))
    time.sleep(0.2)
    print("{:<41}".format("Interests: Gaming, Programming"))
    time.sleep(0.2)
    print(line)


def facebook_get_info():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print("\n{}Waiting for Victim to Login...{}".format(colors.GREEN, colors.END))
    time.sleep(1)
    print("\nVictim Successfully Login.\n")
    time.sleep(1)
    print("\nGetting Facebook Account Information....")
    print("\nEmail Address: kimjoshualopez30@gmail.com")
    print("\nPassword: alawwabalo")
    time.sleep(5)


def getting_gcash():
    os.system("cls" if os.name == "nt" else "clear")
    print("\nWaiting for victim to claim the prize...")
    time.sleep(1)
    print("\nGetting Gcash Information...")
    time.sleep(2)
    print("\nMobile Number: 09518332554")
    time.sleep(2)
    print("\nOTP: 676")
    time.sleep(2)
    print("\n \nSuccessfully hackshesh :>>")


def main():
    victimScan()
    fake_loading()
    fake_credentials()
    time.sleep(10)
    facebook_get_info()
    getting_gcash()


if __name__ == "__main__":
    main()
