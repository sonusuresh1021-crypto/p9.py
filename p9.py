import sys
def check_eligible(days):
    if days <= 7 and days > 0:
        return "eligible"
    else:
        return "not eligible"

if __name__ == "__main__":
    name=sys.argv[1]
    productname=sys.argv[2]
    days=int(sys.argv[3])
 
    result = check_eligible(days)

    print("Name:",name)
    print("productname:",productname)
    print("days:",result)
