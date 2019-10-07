def convert_time_to_secs(n):
    #Have to implement
    #return seconds
    x=n.split(":")
    if len(x)==3:
        hr=int(x[0])*60*60
        min=int(x[1])*60
    elif len(x)==2:
        hr=0
        min=int(x[0])*60
    else:
        hr=0
        min=0
    sec=int(x[-1])
    time=hr+min+sec
    print time
    return time

def validate_password(password):
    #Valdiate given password and return true or false
    pw=len(password)
    i=0
    j=0
    if pw>7:
        try:
            while ord(password[i]) not in (range(ord('a'),ord('z')) or range(ord('A'),ord('Z'))):
                i=i+1
            else:
                while ord(password[j]) not in range(ord('1'),ord('9')):
                    j=j+1
                else:
                    print "valid password"
                    return True
        except:
            print "password must be alphanumeric"
    else:
        print "password is too small"
        return False

def check_armstrong_str(input):
    l=input
    sum=0
    while input!=0:
        k=input%10
        sum=sum+pow(k,3)
        input=input/10
    if l==sum:
        print "armstrong"
        return True
    else:
        print "not armstrong"
        return False

def convert_time_to_24hr_clock(clock):
    x = clock.split()
    if len(x)==2:
        if x[1]=="PM":
            y=x[0].split(":")
            hr=int(y[0])+12
            y[0]=hr
            time=str(y[0])+":"+y[1]+":"+y[2]
            print time
            return time
        else:
            print "time is in AM only"
    else:
        print "time is in 24 hours format"

def convert_secs_to_time_format(n):
    if n >= 3600:
        hr = n / 360
        x = n % 360
        m = x / 60
        s = x % 60
    else:
        hr = 0
        m = n / 60
        s = n % 60
    time = str(hr) + ":" + str(m) + ":" + str(s)
    return time

if __name__ == "__main__":
    time_24hr = convert_time_to_24hr_clock("10:01:30 PM")
    print "24hr time: ",time_24hr
    time_format = convert_secs_to_time_format(10000)
    print "Time : ",time_format

